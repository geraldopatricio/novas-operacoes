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

## packages necessários:
aiohttp==3.7.4.post0<br>
async-timeout==3.0.1<br>
attrs==21.2.0<br>
azure-common==1.1.27<br>
azure-core==1.18.0<br>
azure-identity==1.6.0<br>
azure-keyvault-secrets==4.3.0<br>
azure-storage-file-share==12.5.0<br>
certifi==2021.5.30<br>
cffi==1.14.6<br>
chardet==4.0.0<br>
charset-normalizer==2.0.4<br>
cryptography==3.4.8<br>
idna==3.2<br>
isodate==0.6.0<br>
msal==1.14.0<br>
msal-extensions==0.3.0<br>
msrest==0.6.21<br>
multidict==5.1.0<br>
mysql-connector-python==8.0.26<br>
oauthlib==3.1.1<br>
portalocker==1.7.1<br>
protobuf==3.17.3<br>
pycparser==2.20<br>
PyJWT==2.1.0<br>
pyodbc==4.0.32<br>
requests==2.26.0<br>
requests-oauthlib==1.3.0<br>
six==1.16.0<br>
typing-extensions==3.10.0.2<br>
urllib3==1.26.6<br>
yarl==1.6.3
