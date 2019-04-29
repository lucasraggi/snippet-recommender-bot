import mysql.connector

class MySqlOperator:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            database = 'java_methods',
            passwd = ''
        )
        self.mycursor = self.mydb.cursor()

