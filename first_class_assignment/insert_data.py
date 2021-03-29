import json
import psycopg2
from database_connect_class import DatabaseConnect

keys = []

with open('data/data.json') as file_obj:
    data_json = json.load(file_obj)

for row in data_json:
    for key in row:
        if key not in keys:
            keys.append(key)

print(keys)

len_dict = len(data_json)

create_tbl = """
        CREATE TABLE data_info(
            uuid VARCHAR(50) PRIMARY KEY,
            data VARCHAR(100) NOT NULL,
            min VARCHAR(100) NOT NULL,
            max VARCHAR(100) NOT NULL,
            avg VARCHAR(100) NOT NULL
        )
    """

insert_data = "INSERT INTO data_info(uuid, data, min, max, avg) VALUES ('346','TEMP','0','360','180')"


db_obj = DatabaseConnect()
con = None

try:

    con = db_obj.db_connect()

    con.autocommit = True
    cursor = con.cursor()
    query = "INSERT INTO data_info(uuid, data, min, max, avg) VALUES (%s,%s,%s,%s,%s)"
    

    for i in range(len_dict):
        uuid, data, min, max, avg = data_json[i].values()
        cursor.execute(query, (uuid, data, min, max, avg))


except (Exception, psycopg2.DatabaseError) as error:
        print(error)

finally:
    if con:
        con.close()
        cursor.close()






