import os
from dotenv import load_dotenv
import mysql.connector as mysql
from pymongo import MongoClient
from ..common.my_utils import print_error

load_dotenv()


class Mysql:
    def __init__(self, *args, **kwargs):
        try:
            self.sql_db = mysql.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                user=os.getenv("DB_USERNAME"),
                passwd=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_DATABASE")
            )
            cursor = self.sql_db.cursor()
            cursor.execute('SET GLOBAL wait_timeout=108000')
        except Exception as error:
            print_error(error)

    def insert(self, query):
        try:
            cursor = self.sql_db.cursor()
            cursor.execute(query)
            self.sql_db.commit()
        except Exception as error:
            print_error(error)
        return True

    def insert_many(self, query_list):
        try:
            cursor = self.sql_db.cursor()
            for query in query_list:
                cursor.execute(query)
            self.sql_db.commit()
        except Exception as error:
            print_error(error)
        return True

    def get_column_name(self, query):
        try:
            cursor = self.sql_db.cursor()
            cursor.execute(query)
            column_name = cursor.fetchall()
        except Exception as error:
            print_error(error)
        table_key = [x[0] for x in column_name]
        return table_key

    def get_data(self, query):
        try:
            cursor = self.sql_db.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
        except Exception as error:
            print_error(error)
        return records

    def get_data_as_dict(self, query):
        try:
            cursor = self.sql_db.cursor(dictionary=True)
            cursor.execute(query)
            records = cursor.fetchall()
        except Exception as error:
            print_error(error)
        return records

    def get_single_data_as_dict(self, query):
        try:
            cursor = self.sql_db.cursor(dictionary=True)
            cursor.execute(query)
            records = cursor.fetchone()
        except Exception as error:
            print_error(error)
        return records

    def update(self, query):
        try:
            cursor = self.sql_db.cursor()
            cursor.execute(query)
            self.sql_db.commit()
        except Exception as error:
            print_error(error)
        return True

    def update_many(self, querys):
        try:
            cursor = self.sql_db.cursor()
            for query in querys:
                cursor.execute(query)
            self.sql_db.commit()
        except Exception as error:
            print_error(error)
        return True

    def close(self):
        try:
            cursor = self.sql_db.cursor()
            cursor.close()
        except Exception as error:
            print_error(error)
