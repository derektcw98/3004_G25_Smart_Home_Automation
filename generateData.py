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
            print(day, "\t" + str(x.strftime("%H:%M")), "\t" + str(round(random.uniform(26, 33),2)), "\t" + str(round(random.uniform(60,84),2)), "\t" + str(random.randint(0,1)), "\t" + str(random.randint(0,1)), "\t" + str(random.randint(23,29)), "\ttestRoom")