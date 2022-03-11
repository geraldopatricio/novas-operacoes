## Fluxo do Processo destes Jobs:
<img src="./images/job-rundeck.jpg">

## Info:
## SQLServer
/src/services/db_sqlsrv

## MySQL
/src/services/db_mysql

## SCRIPTS - JOBS a serem rodados
## rodar as 16h
- Para pegar dados do stage e passar para o MySQL
    /src/procedimento_pegar_dados_stage_to_mysql

## rodar as 18h
- Para enviar para o pier através do MySQL
    /src/procedimento_enviar_para_pier

## comandos:
1 -  docker build -t job_operacoes . <br>
2 -  docker run job_operacoes procedimento_pegar_dados_stage_to_mysql.py<br>
3 -  docker run  job_operacoes procedimento_enviar_para_pier.py

