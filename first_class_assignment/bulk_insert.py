import json
import psycopg2
from psycopg2 import extras
from database_connect_class import DatabaseConnect

with open('data/data.json') as file_obj:
    json_data = json.load(file_obj)

create_tbl = """
            CREATE TABLE student_info(
                std_id serial PRIMARY KEY,
                std_name VARCHAR UNIQUE,
                email VARCHAR NOT NULL,
                active bool NOT NULL DEFAULT TRUE
            )
    """

insert_data = """
                INSERT INTO 
                    student_info(std_name, email)
                VALUES(
                    'Imran Khan',
                    'duetboyimran@gmail.com'
                )
                ON CONFLICT (std_name) DO UPDATE 
                SET email='khalekuzzamanimran@gmail.com'
    """


query = """
            INSERT INTO 
                data_info
            VALUES(
                %(uuid)s,
                %(data)s,
                %(min)s,
                %(max)s,
                %(avg)s
            )
            ON CONFLICT DO NOTHING
"""

db_obj = DatabaseConnect()
con = None

try:

    con = db_obj.db_connect()

    con.autocommit = True
    cursor = con.cursor()
    psycopg2.extras.execute_batch(cursor, query, json_data)



except (Exception, psycopg2.DatabaseError) as error:
        print(error)

finally:
    if con:
        con.close()
        cursor.close()

