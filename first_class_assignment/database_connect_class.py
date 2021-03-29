import os
import psycopg2
from dotenv import load_dotenv, find_dotenv


class DatabaseConnect():
    def __init__(self):
        load_dotenv(find_dotenv())
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASS = os.getenv('DB_PASS')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')


    def db_connect(self, db_name=''):
        db = db_name if db_name != '' else self.DB_NAME
        connection = psycopg2.connect(
            host = self.DB_HOST,
            database = db,
            user = self.DB_USER,
            password = self.DB_PASS,
            port = self.DB_PORT
        )

        return connection





