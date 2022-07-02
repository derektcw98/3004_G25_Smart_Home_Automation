import random
import datetime
import pandas

#generate data based on common usual behaviours

#day of week, hour, min, temperature, humidity, light on/off, aircon on/off, aircon temp, room, class

# for step based float random generation
def randfloat(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start

def timeProp(start,l):
   current = start
   curr = current
   while l >= 0:
      curr = curr + datetime.timedelta(minutes=10)
      yield curr
      l-=1

startDate = datetime.datetime(2022, 7, 2, 0,00)
timeDate = datetime.datetime(2022, 7, 1, 23,50)

with open('data.csv', 'w') as f:
    for monthDay in range(0,32):
        for day in range(0,7):
            day = startDate + datetime.timedelta(days= day)
            day  = day.weekday()
            for x in timeProp(timeDate,143): #143 intervals of 10mins in a day

                # bias for temperature and humidity based on time of day
                if int(x.strftime("%H")) >= 7 and int(x.strftime("%H")) <= 19:      # 07 <-> 19 DAY TIME
                    temp = randfloat(32, 36, 0.5)
                    humidity = randfloat(60, 70, 0.5)
                else:                                                               # 00 <-> 06 && 20 <-> 23 NIGHT TIME
                    temp = randfloat(27, 31, 0.5)
                    humidity = randfloat(71, 81, 0.5)

                # bias for TEMPERATURE ONLY to determine aircon state
                if temp >= 32:
                    # bias air con ON 2:1(WD)/9:1(WE)
                    if day <= 4:
                        tempRand = random.randint(1,10)
                    else:
                        tempRand = random.randint(1,3)

                    if tempRand == 1:
                        air_con = 0
                    else:
                        air_con = 1
                else:
                    # bias air con OFF 9:1 
                    tempRand = random.randint(1,10)
                    if tempRand == 1:
                        air_con = 1
                    else:
                        air_con = 0

                # bias for time to determine light state
                if int(x.strftime("%H")) >= 7 and int(x.strftime("%H")) <= 19:      # 07 <-> 19 DAY TIME
                    # bias light OFF 9:1 
                    lightRand = random.randint(1,10)
                    if lightRand == 1:
                        light = 1
                    else:
                        light = 0
                else:                                                               # 00 <-> 06 && 20 <-> 23 NIGHT TIME
                    # bias light ON 9:1
                    lightRand = random.randint(1,10)
                    if lightRand == 1:
                        light = 0
                    else:
                        light = 1

                # set random aircon temperature
                aircon_temp = randfloat(23, 29, 0.5)

                #class generation
                if air_con == 0 and light == 0 and day < 5:
                    label = "wddc"
                elif air_con == 0 and light == 1 and day < 5:
                    label = "wdnc"
                elif air_con == 1 and light == 0 and day < 5: 
                    label = "wddh"
                elif air_con == 1 and light == 1 and day < 5:
                    label = "wdnh"
                elif air_con == 0 and light == 0 and day >= 5:
                    label = "wedc"
                elif air_con == 0 and light == 1 and day >= 5:
                    label = "wenc"
                elif air_con == 1 and light == 0 and day >= 5: 
                    label = "wedh"
                elif air_con == 1 and light == 1 and day >= 5:
                    label = "wenh"

                print(day, "\t" + str(x.strftime("%H")),"\t" + str(x.strftime("%M")), "\t" + str(temp), "\t" + str(humidity), "\t" + str(light), "\t" + str(air_con), "\t" + str(aircon_temp), "\ttestRoom", "\t"+label)
                data = str(day)+ "," + str(x.strftime("%H")) +"," + str(x.strftime("%M"))+ "," + str(temp) + "," + str(humidity) + "," + str(light) + "," + str(air_con) + "," + str(aircon_temp) +","+"testRoom" +","+ label + "\n"
                f.write(data)
