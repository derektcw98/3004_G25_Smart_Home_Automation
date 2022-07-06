import datetime
import pandas as pd
import sqlalchemy

# pip install mysqlclient
# access mariadb
# mysql --host=192.168.1.16 --port=3306 -u root -p


def engine(host, port, database, user, password):
    engine = sqlalchemy.create_engine(
        f"mysql+mysqldb://{user}:{password}@{host}/{database}", pool_recycle=3600)

    if engine.connect():
        print("Connected")
    else:
        print("Failed to connect")    
    return engine

def insert(engine):
    # create table for sensor
    # engine.execute("create table if not exists sensors (sensor_id int primary key NOT NULL AUTO_INCREMENT, day int NOT NULL, hour int NOT NULL, minute int NOT NULL, temperature double NOT NULL, humidity double NOT NULL, light_state bit(1) NOT NULL, aircon_state bit(1) NOT NULL, aircon_temp int NOT NULL, room varchar(9) NOT NULL, label char(4) NOT NULL)")

    # dataframe into mariadb
    with engine.begin() as conn:
        df = pd.read_csv('modelGenNPred/models/data.csv')
        df.columns = ["day", "hour", "minute", "temperature", "humidity",
                      "light_state", "aircon_state", "aircon_temp", "room", "label"]
        now = datetime.datetime.now().date()
        df['date'] = now
        df.to_sql('sensors', conn, if_exists='append', index=False)
        print("Inserted")


if __name__ == '__main__':
    #need to change local host to ip of Db
    engine = engine('localhost', 3306, 'homedb', 'root', 'mariasama')
    engine.execute("create table if not exists sensors (date DATE NOT NULL, day int NOT NULL, hour int NOT NULL, minute int NOT NULL, temperature double NOT NULL, humidity double NOT NULL, light_state tinyint(1) NOT NULL, aircon_state tinyint(1) NOT NULL, aircon_temp int NOT NULL, room varchar(9) NOT NULL, label char(4) NOT NULL)")
    insert(engine)

# weekly csv file using sensorlogger.py > save into containerised maria > query week/month's worth of data
