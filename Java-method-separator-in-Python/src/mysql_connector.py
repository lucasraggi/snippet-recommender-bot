import mysql.connector

class MySqlOperator:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            database = 'java_methods',
            passwd = 'ARTHURESAX9512357'
        )
        self.mycursor = self.mydb.cursor()

    def insert_table(self, codes):
        try:
            for i in codes:
                method_name = str(i.name)
                method_codes = '\n'.join(map(str, i.code_lines))
                self.mycursor.execute('insert into methods(name, codes) values(%s, %s)', (method_name, method_codes))
        except mysql.connector.Error as err:
            print("ERROR in insert table {}".format(err))

    def select_table_from_name(self, method_name):
        try:
            self.mycursor.execute('select codes from methods where name = %s', (method_name,))
            return self.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("ERROR in select tablem from table {}".format(err))

    def commit_table(self):
        try:
            self.mydb.commit()
            self.mydb.close()
        except mysql.connector.Error as err:
            print("ERROR in commit table {}".format(err))

