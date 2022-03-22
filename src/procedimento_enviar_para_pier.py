from services.db_mysql import MySQL
from services.pier import Pier
from jobs.processar_arquivo import handle_request

db_servicos = MySQL()
pier = Pier()

cursor = db_servicos.connect()

cmd = "SELECT id, idEstabelecimento, idOperacao, idProduto, mcc, flagoperacao FROM jobs_operacoes where data_envio_api is null"

cursor.execute(cmd)

registros = cursor.fetchall()

for registro in registros:
    
    status, url = handle_request(registro, pier)

    id, *resto = registro

    mensagem = f"{status} - registro enviado com sucesso" if status == 200 else f"{status} - registro não enviado"
    
    #update with date
    cmd_update = """
        UPDATE NOMEDATABELA
        SET data_envio_api = now(),
        nome_arquivo = %s
        WHERE
        id = %s
    """
    valores = (mensagem, id)

    cursor.execute(cmd_update, valores)
    cursor.fetchall() #apenas para zerar cursor
    db_servicos.commit()
cursor.close()
db_servicos.close()
print("Finalizado com sucesso")
