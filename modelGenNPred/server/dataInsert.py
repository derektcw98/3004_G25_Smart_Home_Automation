import datetime
import pandas as pd
import sqlalchemy

# pip install mysqlclient
# access mariadb
# mysql --host=192.168.1.16 --port=3306 -u root -p


def engine(): #TODO:remove params
    engine = sqlalchemy.create_engine(
        #TODO: replace user, password, host, database to environmental variables
        f"mysql+mysqldb://root:mariasama@192.168.1.24:3306/homedb", pool_recycle=3600) 

    if engine.connect():
        print("Connected")
    else:
        print("Failed to connect")    
    return engine

def insert(filepath):
    conn = engine()
    conn.execute("create table if not exists sensors (date DATE NOT NULL, day int NOT NULL, hour int NOT NULL, minute int NOT NULL, temperature double NOT NULL, humidity double NOT NULL, light_state tinyint(1) NOT NULL, aircon_state tinyint(1) NOT NULL, aircon_temp int NOT NULL, room varchar(9) NOT NULL, label char(4) NOT NULL)")
    # create table for sensor
    # engine.execute("create table if not exists sensors (sensor_id int primary key NOT NULL AUTO_INCREMENT, day int NOT NULL, hour int NOT NULL, minute int NOT NULL, temperature double NOT NULL, humidity double NOT NULL, light_state bit(1) NOT NULL, aircon_state bit(1) NOT NULL, aircon_temp int NOT NULL, room varchar(9) NOT NULL, label char(4) NOT NULL)")

    # dataframe into mariadb
    with conn.begin() as conn:
        df = pd.read_csv(filepath)
        df.columns = ["day", "hour", "minute", "temperature", "humidity",
                      "light_state", "aircon_state", "aircon_temp", "room", "label"]
        now = datetime.datetime.now().date()
        df['date'] = now
        df.to_sql('sensors', conn, if_exists='append', index=False)
        print("Inserted")

# weekly csv file using sensorlogger.py > save into containerised maria > query week/month's worth of data