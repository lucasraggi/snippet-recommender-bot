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

    def insert_table(self, codes):
        try:
            for i in codes:
                method_name = str(i.name)
                method_codes = '\n'.join(map(str, i.code_lines))
                class_name = str(i.class_name)
                self.mycursor.execute('insert into methods(name, class, method) values(%s, %s, %s)',
                                      (method_name, class_name, method_codes))
        except mysql.connector.Error as err:
            print("ERROR in insert table {}".format(err))

    def select_table_from_name(self, method_name):
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

    def commit_table(self):
        try:
            self.mydb.commit()
        except mysql.connector.Error as err:
            self.mydb.commit()
            print("ERROR in commit table {}".format(err))

    def close_connection(self):
        self.mydb.close()

    def reset_query_cache(self):
        self.mycursor.execute('RESET QUERY CACHE')
