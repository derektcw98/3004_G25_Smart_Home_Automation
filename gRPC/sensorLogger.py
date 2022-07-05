from time import sleep
from sense_hat import SenseHat
import os
from datetime import datetime, timedelta
from pathlib import Path
import threading
import random
import sys
sense = SenseHat()

events = {}

interval_secs = 1*60

# Entry Inits
now = datetime.now()
dayOfWeek = 0
dayHour = 0
dayMin = 0
temperature = 0
humidity = 0
AC = False
AC_State = 0
Light = False
Light_State = 0
AC_Temp = 0
if len(sys.argv)==2:
  room = sys.argv[1]
else:
  room = "Default_Room"
label = ""

# Saving of sensor data function
def saveSensorData():
  global dayOfWeek,dayHour,dayMin,temperature,humidity,AC_State,Light_State,AC_Temp,room,label
  # Save if 10 minute mark
  curr_min = int(datetime.now().strftime("%M")[1:])
  if curr_min==0:

    #creates file if it doesn't exists
    now = datetime.now()
    dayOfWeek = int(now.weekday())
    now_dmy = now.strftime("%d%m%Y")
    file_path = room + "_" + str(now_dmy) + ".csv"
    
    if dayOfWeek == 0 and not Path(file_path).exists:
      file = Path(file_path)
      file.touch(exist_ok=True)
    
    # for days besides monday, assign file_path to monday's date
    if dayOfWeek!=0:
      startOfWeek_dmy = (datetime.now() - timedelta(days=dayOfWeek)).strftime("%d%m%Y")
      file_path = room + "_" + str(startOfWeek_dmy) + ".csv"
      
    # get variables to save
    dayHour = int(datetime.now().strftime("%H"))
    dayMin = int(datetime.now().strftime("%M"))
    sensehat_temp = sense.get_temperature()
    temperature = str(round((temp - ((get_cpu_temp() - temp)/2.466)), 2))
    humidity = str(round(sense.get_humidity(),2))
    if AC_State == 0 and Light_State == 0:
        label = "nanl"
    elif AC_State == 0 and Light_State == 1:
        label = "nagl"
    elif AC_State == 1 and Light_State == 0: 
        label = "ganl"
    elif AC_State == 1 and Light_State == 1:
        label = "gagl"

    # form new entry
    entry = ""
    entry += str(dayOfWeek) + ","
    entry += str(dayHour) + ","
    entry += str(dayMin) + ","
    entry += str(temperature) + ","
    entry += str(humidity) + ","
    entry += str(AC_State) + ","
    entry += str(Light_State) + ","
    entry += str(AC_Temp) + ","
    entry += str(room) + ","
    entry += str(label) + "\n"

    with open(file_path, "a") as file:
      print("current time: ", datetime.now().strftime("%H:%M:%S"))
      print("writing: ", entry)
      file.write(entry)

def startSensorLogger():
  threading.Timer(interval_secs, startSensorLogger).start()
  saveSensorData()

def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

# for step based float random generation
def randfloat(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start

startSensorLogger()

sense.clear()
while True:
  sleep(1)
  for event in sense.stick.get_events(): #on joystick press do action

    # Air-Conditioner TOGGLE
    if event.direction == "up" and event.action == "pressed":
      AC = not AC
      if AC == True:
        AC_State = 1
      else:
        AC_State = 0  

    # Light TOGGLE
    if event.direction == "down" and event.action == "pressed":
      Light = not Light
      if Light == True:
        Light_State = 1
      else:
        Light_State = 0
    
    # display user action
    print(event.direction, event.action)

    # on release, show all states
    if event.action == "released":
      print("AC State: " + AC_State)
      print("Light State: " + Light_State)

