from services.metasingleton import MetaSingleton
from services.safebox import Safebox
import pyodbc

class SQLServer(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            server = Safebox.get_secret("DB-STAGE-HOST")
            database = Safebox.get_secret("DB-STAGE-DATABASE")
            username = Safebox.get_secret("DB-STAGE-RDKVINCULOSPRODUTOS-USERNAME")
            password = Safebox.get_secret("DB-STAGE-RDKVINCULOSPRODUTOS-PASSWORD")
            string_connection = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
            self.connection = pyodbc.connect(string_connection)
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

    def close(self):
        self.connection.close()