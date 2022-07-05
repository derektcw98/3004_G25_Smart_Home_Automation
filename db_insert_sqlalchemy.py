import datetime
import pandas as pd
import sqlalchemy

# pip install mysqlclient
# access mariadb
# mysql --host=192.168.1.16 --port=3306 -u root -p


def engine(host, port, database, user, password):
    engine = engine = sqlalchemy.create_engine(
        f"mysql+mysqldb://{user}:{password}@{host}/{database}", pool_recycle=3600)

    if engine.connect():
        print("Connected")
    else:
        print("Failed to connect")    
    return engine

def insert(engine):
    # create table for sensor
    # engine.execute("create table if not exists sensors (sensor_id int primary key NOT NULL AUTO_INCREMENT, day int NOT NULL, hour int NOT NULL, minute int NOT NULL, temperature double NOT NULL, humidity double NOT NULL, light_state bit(1) NOT NULL, aircon_state bit(1) NOT NULL, aircon_temp int NOT NULL, room varchar(9) NOT NULL, class char(4) NOT NULL)")

    # dataframe into mariadb
    with engine.begin() as conn:
        df = pd.read_csv('models/data.csv')
        df.columns = ["day", "hour", "minute", "temperature", "humidity",
                      "light_state", "aircon_state", "aircon_temp", "room", "class"]
        now = datetime.datetime.now().date()
        df['date'] = now
        df.to_sql('sensors', conn, if_exists='append', index=False)
        print("Inserted")

    # my pc is getting 'mariadb.ProgrammingError: Cursor is closed', but it fine on my laptop/pi
    # issue could just be mariadb not being installed on my pc but doubt so cus i could still execute create table

def queryRoom(engine, room):
    conn = engine.raw_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM sensors\
        WHERE room = %s\
        LIMIT 15", (room,))
    rows = c.fetchall()
    for row in rows:
        print(row)


def retrieveMonthPandas(engine, room):
    conn = engine.raw_connection()
    c = conn.cursor()
    query = """SELECT day, hour, minute, temperature, humidity, light_state, aircon_state, aircon_temp, room, class from sensors where room = %(roomname)s AND date(date) between (curdate() - interval 1 month) and curdate() limit 15"""

    df = pd.read_sql_query(sql=query, con=engine, params={"roomname": room})
    df.to_csv('noclass.csv', index=False, header=None)
    print("noclass.csv written")


if __name__ == '__main__':
    engine = engine('localhost', 3306, 'homedb', 'root', 'mariasama')
    engine.execute("create table if not exists sensors (date DATE NOT NULL, day int NOT NULL, hour int NOT NULL, minute int NOT NULL, temperature double NOT NULL, humidity double NOT NULL, light_state tinyint(1) NOT NULL, aircon_state tinyint(1) NOT NULL, aircon_temp int NOT NULL, room varchar(9) NOT NULL, class char(4) NOT NULL)")
    insert(engine)
    retrieveMonthPandas(engine, input("Query room: "))

# weekly csv file using sensorlogger.py > save into containerised maria > query week/month's worth of data
