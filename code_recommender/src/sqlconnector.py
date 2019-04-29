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

    def select_name_from_table(self, method_name):
        try:
            self.mycursor.execute('select codes from methods where name = %s', (method_name,))
            return self.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("ERROR in select table from table {}".format(err))

    def select_class_and_name_from_table(self):
        try:
            self.mycursor.execute('SELECT name, class from methods')
            return self.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('ERROR in select name and class {}'.format(err))

    def close_connection(self):
        self.mydb.close()

    def reset_query_cache(self):
        self.mycursor.execute('RESET QUERY CACHE')


