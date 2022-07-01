import csv
import pandas as pd
import mysql.connector

class Database():
    cnx = None
    cursor = None

    def __init__(self, host, port, database, user, password):
        self.cnx = self.establishconnection(host, port, database, user, password)

    # host: url (eg. localhost)
    # port: portnumber
    # database: name of database to connect into
    # user: db user name
    # password: password of the db user
    def establishconnection(self, _host, _port, _database, _user, _password):
        cnx = mysql.connector.connect(
        host=_host,
        port=_port,
        database=_database,
        user=_user,
        password=_password
    )

        if cnx.is_connected():
            db_Info = cnx.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            self.cursor = cnx.cursor()
            return cnx
   
    def execute(self, query):
        self.cursor.execute(query)

    def fetchQuery(self, query):
        cursor = self.cnx.cursor()
        cursor.execute(query)
        return list(cursor.fetchall())

if __name__ == '__main__':
    db = Database('localhost', 3306, 'homedb', 'root', 'mA1d1n90ran93')
    
    data = pd.read_csv('data.csv')
    columns = ["day", "hour", "minute", "temperature", "humidity", "light_state", "aircon_state", "aircon_temp", "room", "class"]
    data.columns = columns
    db.execute("create table if not exists sensors (sensor_id int primary key NOT NULL, day int NOT NULL, hour int NOT NULL, minute int NOT NULL,   temperature double NOT NULL, humidity double NOT NULL, light_state bit(1) NOT NULL, aircon_state bit(1) NOT NULL, aircon_temp int NOT NULL, room varchar(9) NOT NULL, class char(4) NOT NULL)")
    

