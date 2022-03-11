"""
    Procedimento:
    1 - instanciar o banco de dados SQLServer
    2 - instanciar banco de dados MYSQL
    3 - Fazer consulta de dados no SQLserver
    4 - De linha a linha registrar no MYSQL

    campos sqlsrv: 
    campos mysql :
"""
from services.db_sqlsrv import SQLServer
from services.db_mysql import MySQL

stage = SQLServer()
db_servicos = MySQL()

stage_cursor = stage.connect()

db_servicos_cursor = db_servicos.connect()

# consulta que irá trazer os produtos novos a serem incluídos nos estabelecimentos
cmd = """   
SELECT  L.ID_ESTABELECIMENTO AS IDESTABELECIMENTO, 
            CASE L.QT_MAX_PARCELA
                WHEN '0' THEN '19'
                WHEN '1' THEN '19'
                WHEN ' ' THEN '19'
                WHEN '' THEN '19'
                WHEN '2' THEN '168'
                WHEN '3' THEN '144'
                WHEN '4' THEN '145'
                WHEN '5' THEN '145'
                WHEN '6' THEN '145'
                WHEN '7' THEN '146'
                WHEN '8' THEN '146'
                WHEN '9' THEN '146'
                WHEN '10' THEN '146'
                WHEN '11' THEN '10125'
                WHEN '12' THEN '10125'
                WHEN '13' THEN '10125'
                WHEN '31' THEN '10125'
                WHEN '38' THEN '10125'
                WHEN '96' THEN '10125'
                ELSE '19'
            END IDOPERACAO, 
            (SELECT TOP 1 
                    (ID_PRODUTO) 
            FROM CDT_T_PRODUTO 
            ORDER BY ID_PRODUTO DESC) AS IDPRODUTO, 
            CASE (SELECT TOP 1 
                (P.CD_BIN) 
                FROM CDT_T_PRODUTO 
                ORDER BY ID_PRODUTO DESC)
                WHEN '230888' THEN '9999'
                WHEN '628167' THEN '0'
                ELSE 'NONE'
            END MCC, 
            (1) FLAGOPERACAO
    FROM VI_DW_T_LOJA L 
    INNER JOIN CDT_T_PRODUTO P ON P.ID_PRODUTO = L.ID_PRODUTO
    WHERE L.DT_CANCELAMENTO IS NULL
    AND P.CD_BIN IN ('230888','628167')

    UNION

    SELECT  L.ID_ESTABELECIMENTO AS IDESTABELECIMENTO, 
            (24) IDOPERACAO, 
            (SELECT TOP 1 
                    (ID_PRODUTO) 
            FROM CDT_T_PRODUTO 
            ORDER BY ID_PRODUTO DESC) AS IDPRODUTO, 
            CASE (SELECT TOP 1 
                (P.CD_BIN) 
                FROM CDT_T_PRODUTO 
                ORDER BY ID_PRODUTO DESC)
                WHEN '230888' THEN '9999'
                WHEN '628167' THEN '0'
                ELSE 'NONE'
            END MCC, 
            (1) FLAGOPERCAO
    FROM VI_DW_T_LOJA L 
    INNER JOIN CDT_T_PRODUTO P ON P.ID_PRODUTO = L.ID_PRODUTO
    WHERE L.DT_CANCELAMENTO IS NULL
    AND P.CD_BIN IN ('230888','628167')

    UNION

    SELECT  L.ID_ESTABELECIMENTO AS IDESTABELECIMENTO, 
            (19) IDOPERACAO, 
            (SELECT TOP 1 
                    (ID_PRODUTO) 
            FROM CDT_T_PRODUTO 
            ORDER BY ID_PRODUTO DESC) AS IDPRODUTO, 
            CASE (SELECT TOP 1 
                (P.CD_BIN) 
                FROM CDT_T_PRODUTO 
                ORDER BY ID_PRODUTO DESC)
                WHEN '230888' THEN '9999'
                WHEN '628167' THEN '0'
                ELSE 'NONE'
            END MCC, 
            (1) FLAGOPERCAO
    FROM VI_DW_T_LOJA L 
    INNER JOIN CDT_T_PRODUTO P ON P.ID_PRODUTO = L.ID_PRODUTO
    WHERE L.DT_CANCELAMENTO IS NULL
    AND P.CD_BIN IN ('230888','628167')
    AND L.QT_MAX_PARCELA in ('2','3','4','5','6','7','8','9','10','11','12','13','31','38','96')
    
    """

stage_cursor.execute(cmd)

registros = stage_cursor.fetchall()

#converter cada registro para uma tupla, que é o que o mysql aceita para fazer execute many [(idestabelecimento, idoperacao, idproduto, mcc, flagoperacao)]
data = [(registro.IDESTABELECIMENTO, registro.IDOPERACAO, registro.IDPRODUTO, registro.MCC, registro.FLAGOPERACAO) for registro in registros]

insert_query = """
    insert into jobs_operacoes (idEstabelecimento, idOperacao, idProduto, mcc, flagOperacao, nome_arquivo) values (%s, %s, %s, %s, %s , now());
"""

db_servicos_cursor.executemany(insert_query, data)

db_servicos.commit()

print("Finalizado com sucesso")
