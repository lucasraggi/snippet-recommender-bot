import mysql.connector

class MySqlOperator:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            database = 'java_codes_recommender',
            passwd = ''
        )
        self.mycursor = self.mydb.cursor()
        self.create_database()
        self.create_table()

    def create_database(self):
        try:
            self.mycursor.execute('CREATE DATABASE IF NOT EXISTS java_codes_recommender')
        except mysql.connector.Error as err:
            print('ERROR in create database {}'.format(err))

    def create_table(self):
        try:
            self.mycursor.execute('CREATE TABLE IF NOT EXISTS methods ('
                                  'id int not null auto_increment,'
                                  'method_name varchar(255),'
                                  'code longtext, '
                                  'number_parameters int,'
                                  'parameters_types varchar(255),'
                                  'return_type varchar(255),'
                                  'primary key (id)) default char set utf8mb4;')
        except mysql.connector.Error as err:
            print('ERROR in create table {}'.format(err))

    def insert_table(self, method_name, code, number_parameters, parameter_types, return_type):
        try:
            self.mycursor.execute('INSERT INTO METHODS (method_name, code, number_parameters, parameters_type, return_type)'
                                  'values(%s, %s, %s, %s, %s)',(method_name, code, number_parameters, parameter_types, return_type))
        except mysql.connector.Error as err:
            print("ERROR in insert table {}".format(err))

    def select_method(self, method_name):
        try:
            self.mycursor.execute('SELECT CODES FROM methods WHERE NAME = %s', (method_name,))
            return self.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("ERROR in select table from table {}".format(err))

    def close_connection(self):
        self.mydb.close()

    def reset_query_cache(self):
        self.mycursor.execute('RESET QUERY CACHE')

