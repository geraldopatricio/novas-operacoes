from services.metasingleton import MetaSingleton
import mysql.connector
from services.safebox import Safebox

class MySQL(metaclass=MetaSingleton):
    connection = None
          
    def connect(self):
        if self.connection is None:            
            host = Safebox.get_secret("DB-SERVICOS-HOST")
            login = Safebox.get_secret("DB-SERVICOS-RDKJOBOPERACOES-USERNAME")
            password = Safebox.get_secret("DB-SERVICOS-RDKJOBOPERACOES-PASSWORD")
            database =  Safebox.get_secret("DB-SERVICOS-DATABASE")
            login= f"{login}@{host}"
            self.connection = mysql.connector.connect(host=host, user=login, passwd=password, database=database)
            self.cursorobj = self.connection.cursor()
        return self.cursorobj 

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
    
    def commit(self):
        self.connection.commit()
