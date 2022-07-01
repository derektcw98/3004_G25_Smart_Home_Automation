from matplotlib.pyplot import connect
import pandas as pd
import sqlalchemy

# access mariadb
# mysql --host=192.168.1.16 --port=3306 -u root -p


def engine():
    engine = engine = sqlalchemy.create_engine(
        "mariadb+mariadbconnector://root:mariasama@192.168.1.16:3306/homedb", pool_recycle=3600)
    print(engine)
    return engine


def dropTable(engine):
    conn = engine.raw_connection()
    c = conn.cursor()
    c.execute("DROP table sensors")


def insert(engine):
    # create table for sensor
    engine.execute("create table if not exists sensors (sensor_id int primary key NOT NULL AUTO_INCREMENT, day int NOT NULL, hour int NOT NULL, minute int NOT NULL, temperature double NOT NULL, humidity double NOT NULL, light_state bit(1) NOT NULL, aircon_state bit(1) NOT NULL, aircon_temp int NOT NULL, room varchar(9) NOT NULL, class char(4) NOT NULL)")

    # dataframe into mariadb
    with engine.begin() as conn:
        df = pd.read_csv('data.csv')
        df.columns = ["day", "hour", "minute", "temperature", "humidity",
                      "light_state", "aircon_state", "aircon_temp", "room", "class"]
        df.to_sql('sensors', conn, if_exists='append', index=False)
        print("Inserted")

    # my pc is getting 'mariadb.ProgrammingError: Cursor is closed', but it fine on my laptop
    # issue could just be mariadb not being installed on my pc but doubt so cus i could still execute create table


def queryRoom(engine, room):
    conn = engine.raw_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM sensors WHERE room = %s LIMIT 15", (room,))
    # c.execute("SELECT * FROM sensors WHERE room = 'testRoom' LIMIT 15")
    # query = "SELECT * FROM sensors WHERE room = 'testRoom' LIMIT 15"
    # c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    engine = engine()
    insert(engine)
    queryRoom(engine, input("Query room: "))

# weekly csv file using sensorlogger.py > save into containerised maria > query week/month's worth of data
