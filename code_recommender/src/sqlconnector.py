import mysql.connector

class MySqlOperator:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            passwd = ''
        )
        self.mycursor = self.mydb.cursor()
        self.create_database()
        self.create_table()

    def create_database(self):
        try:
            self.mycursor.execute('CREATE DATABASE IF NOT EXISTS java_codes_recommender')
            self.mycursor.execute('USE java_codes_recommender')
        except mysql.connector.Error as err:
            print('ERROR in create database {}'.format(err))

    def create_table(self):
        try:
            self.mycursor.execute('CREATE TABLE IF NOT EXISTS methods ('
                                  'id int not null auto_increment,'
                                  'class_name varchar(255),'
                                  'method_name varchar(255),'
                                  'code longtext, '
                                  'number_parameters int,'
                                  'parameters_types varchar(255),'
                                  'return_type varchar(255),'
                                  'primary key (id)) default char set utf8mb4;')
        except mysql.connector.Error as err:
            print('ERROR in create table {}'.format(err))

    def insert_table(self, class_name, method_name, code, number_parameters, parameter_types, return_type):
        try:
            self.mycursor.execute('INSERT INTO methods (class_name, method_name, code, number_parameters, parameters_types, return_type) '
                                  'values(%s, %s, %s, %s, %s, %s)',(class_name, method_name, code, number_parameters, parameter_types, return_type))
        except mysql.connector.Error as err:
            print("ERROR in insert table {}".format(err))

    def select_method(self, method_name):
        try:
            self.mycursor.execute('SELECT * FROM methods WHERE method_name = %s', (method_name,))
            return self.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("ERROR in select table from table {}".format(err))

    def close_connection(self):
        self.mydb.close()

    def commit_table(self):
        try:
            self.mydb.commit()
        except mysql.connector.Error as err:
            self.mydb.commit()
            print("ERROR in commit table {}".format(err))

    def reset_query_cache(self):
        self.mycursor.execute('RESET QUERY CACHE')
