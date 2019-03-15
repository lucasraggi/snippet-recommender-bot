import mysql.connector

class MySqlOperator:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host = '127.0.0.1',
                user = 'root',
                database = 'java',
                passwd = ''
            )
            self.mycursor = self.mydb.cursor()
        except mysql.connector.Error as err:
            print("ERROR to connect in database {}".format(err))

    def insert_table(self, codes):
        try:
            for i in codes:
                method_name = str(i.name)
                method_codes = '\n'.join(map(str, i.code_lines))
                class_name = str(i.class_name)
                self.mycursor.execute('insert into methods(name, class, codes) values(%s, %s, %s)',
                                      (method_name, class_name, method_codes))
        except mysql.connector.Error as err:
            print("ERROR in insert table {}".format(err))

    def select_table_from_name(self, method_name):
        try:
            self.mycursor.execute('select codes from methods where name = %s', (method_name,))
            return self.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("ERROR in select table from table {}".format(err))

    def commit_table(self):
        try:
            self.mydb.commit()
            self.mydb.close()
        except mysql.connector.Error as err:
            print("ERROR in commit table {}".format(err))

