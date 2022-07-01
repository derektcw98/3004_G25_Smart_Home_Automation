import random
import datetime

#generate data based on common usual behaviours

#day of week, time, temperature, humidity, light on/off, aircon on/off, aircon temp, room, class

def timeProp(start,l):
   current = start
   curr = current
   while l >= 0:
      curr = curr + datetime.timedelta(minutes=10)
      yield curr
      l-=1

startDate = datetime.datetime(2022, 6, 27,0,00)
timeDate = datetime.datetime(2022, 6, 26,23,50)
for monthDay in range(0,4):
    for day in range(0,7):
        day = startDate + datetime.timedelta(days= day)
        day  = day.weekday()
        for x in timeProp(timeDate,143): #143 intervals of 10mins in a day
            #bias for temperature and humidity based on time of day
            if int(x.strftime("%H")) >= 10 and int(x.strftime("%H")) <= 19:
                temp = round(random.uniform(30, 38),2)
                humidity = round(random.uniform(60,80),2)
            else:
                temp = round(random.uniform(27, 34),2)
                humidity = round(random.uniform(70,96),2)
            #bias for temperature generation to determine aircon state
            if temp > 25 and humidity > 70:
                tempRand = random.randint(1,10)
                if tempRand < 2:
                    air_con = 0
                else:
                    air_con = 1
            else:
                tempRand = random.randint(1,10)
                if tempRand < 2:
                    air_con = 1
                else:
                    air_con = 0
            #bias for time to determine light state
            if int(x.strftime("%H")) >= 19 and int(x.strftime("%H")) <= 7:
                lightRand = random.randint(1,10)
                if lightRand < 2:
                    light = 0
                else:
                    light = 1
            else:
                lightRand = random.randint(1,10)
                if lightRand < 2:
                    light = 1
                else:
                    light = 0
            aircon_temp = random.randint(23,29)
            print(day, "\t" + str(x.strftime("%H:%M")), "\t" + str(temp), "\t" + str(humidity), "\t" + str(light), "\t" + str(air_con), "\t" + str(aircon_temp), "\ttestRoom")