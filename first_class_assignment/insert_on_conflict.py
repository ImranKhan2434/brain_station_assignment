import json
import psycopg2
from database_connect_class import DatabaseConnect

query = """
            CREATE TABLE student_info(
                std_id serial PRIMARY KEY,
                std_name VARCHAR UNIQUE,
                email VARCHAR NOT NULL,
                active bool NOT NULL DEFAULT TRUE
            )
    """

db_obj = DatabaseConnect()
con = None

try:

    con = db_obj.db_connect()

    con.autocommit = True
    cursor = con.cursor()

    query = """
                INSERT INTO 
                    student_info(std_name, email)
                VALUES(
                    'Khan',
                    'duetboyimran@gmail.com'
                )
                ON CONFLICT (std_name) DO NOTHING
    """

    cursor.execute(query)


except (Exception, psycopg2.DatabaseError) as error:
        print(error)

finally:
    if con:
        con.close()
        cursor.close()

