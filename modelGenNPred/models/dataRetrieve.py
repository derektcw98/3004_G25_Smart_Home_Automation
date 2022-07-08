from datetime import datetime, timedelta
from time import sleep
import pandas as pd
import sqlalchemy
from generateModel import generateModel
from pathlib import Path

# pip install mysqlclient
# access mariadb
# mysql --host=192.168.1.16 --port=3306 -u root -p

# TODO: once a week run to pull data from db and save as respective csv


def engine(host, port, database, user, password):
    engine = sqlalchemy.create_engine(
        f"mysql+mysqldb://{user}:{password}@{host}:{port}/{database}", pool_recycle=3600)

    if engine.connect():
        print("Connected")
    else:
        print("Failed to connect")
    return engine


def retrieveWeekPandas(engine, room):
    conn = engine.raw_connection()
    c = conn.cursor()
    query = """SELECT day, hour, minute, temperature, humidity, aircon_temp, room, label from sensors where room = %(roomname)s AND date(date) between (curdate() - interval 1 week) and (curdate() + interval 1 day)"""

    weekDF = pd.read_sql_query(
        sql=query, con=engine, params={"roomname": room})
    return weekDF


def retrieveMonthPandas(engine, room):
    conn = engine.raw_connection()
    c = conn.cursor()
    query = """SELECT day, hour, minute, temperature, humidity, aircon_temp, room, label from sensors where room = %(roomname)s AND date(date) between (curdate() - interval 1 month) and (curdate() + interval 1 day)"""

    monthDF = pd.read_sql_query(
        sql=query, con=engine, params={"roomname": room})
    return monthDF


def retrieve2MonthPandas(engine, room):
    # TODO: SQL query to pull (up to 2 months of records, 8,064 records ) from startOfWeek_dmy
    # Save above to a dataframe object twoMonthDF
    conn = engine.raw_connection()
    c = conn.cursor()
    query = """SELECT day, hour, minute, temperature, humidity, aircon_temp, room, label from sensors where room = %(roomname)s AND date(date) between (curdate() - interval 2 month) and (curdate() + interval 1 day)"""

    twoMonthDF = pd.read_sql_query(
        sql=query, con=engine, params={"roomname": room})
    return twoMonthDF


if __name__ == '__main__':
    # localhost should be replaced with env variable
    engine = engine('192.168.1.24', 3306, 'homedb', 'root', 'mariasama')
    engine.execute("create table if not exists sensors (date DATE NOT NULL, day int NOT NULL, hour int NOT NULL, minute int NOT NULL, temperature double NOT NULL, humidity double NOT NULL, light_state tinyint(1) NOT NULL, aircon_state tinyint(1) NOT NULL, aircon_temp int NOT NULL, room varchar(9) NOT NULL, label char(4) NOT NULL)")
    while True:
        now = datetime.now()
        dayOfWeek = int(now.weekday())
        dayHour = int(datetime.now().strftime("%H"))

        # Check if client time matches : Monday 02:00
        if dayOfWeek == 0 and dayHour == 2:
            # Get datetime for SQL query
            startOfWeek_dmy = (
                datetime.now() - timedelta(days=7)).strftime("%d%m%Y")
            uniqueRooms = []
            roomsDict = {}
            # SQL query to get the unique rooms
            # Save above to a dataframe object roomDF
            query = """SELECT DISTINCT room from sensors;"""
            roomDF = pd.read_sql_query(sql=query, con=engine)
            # Iterate room names in roomDF to uniqueRooms
            # For loop of uniqueRooms to add respective dataframe
            for room in roomDF['room']:
                roomData = retrieveMonthPandas(engine, room)
                roomsDict[room] = roomData
                file_path = room + "_training_data.csv"
                file_path = Path(file_path)
                file_path.touch(exist_ok=True)
                with  open(file_path, 'w') as file:
                    file.write(roomData.to_string())
                print(file_path+" written.")

            for roomKey in roomsDict:
                generateModel(roomKey, roomsDict[roomKey])

        sleep(1*60*60)

    # retrieveMonthPandas(engine, input("Query room: "))

# weekly csv file using sensorlogger.py > save into containerised maria > query week/month's worth of data
