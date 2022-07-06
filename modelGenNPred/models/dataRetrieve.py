import datetime
import pandas as pd
import sqlalchemy

# pip install mysqlclient
# access mariadb
# mysql --host=192.168.1.16 --port=3306 -u root -p

# TODO: once a week run to pull data from db and save as respective csv

def engine(host, port, database, user, password):
    engine = sqlalchemy.create_engine(
        f"mysql+mysqldb://{user}:{password}@{host}/{database}", pool_recycle=3600)

    if engine.connect():
        print("Connected")
    else:
        print("Failed to connect")    
    return engine

def retrieveMonthPandas(engine, room):
    conn = engine.raw_connection()
    c = conn.cursor()
    query = """SELECT day, hour, minute, temperature, humidity, light_state, aircon_state, aircon_temp, room from sensors where room = %(roomname)s AND date(date) between (curdate() - interval 1 month) and curdate()"""

    df = pd.read_sql_query(sql=query, con=engine, params={"roomname": room})
    df.to_csv('test.csv', index=False, header=None)
    print("noclass.csv written")


if __name__ == '__main__':
    #localhost should be replaced with env variable
    engine = engine('localhost', 3306, 'homedb', 'root', 'mypass')
    engine.execute("create table if not exists sensors (date DATE NOT NULL, day int NOT NULL, hour int NOT NULL, minute int NOT NULL, temperature double NOT NULL, humidity double NOT NULL, light_state tinyint(1) NOT NULL, aircon_state tinyint(1) NOT NULL, aircon_temp int NOT NULL, room varchar(9) NOT NULL, class char(4) NOT NULL)")
    retrieveMonthPandas(engine, input("Query room: "))

# weekly csv file using sensorlogger.py > save into containerised maria > query week/month's worth of data
