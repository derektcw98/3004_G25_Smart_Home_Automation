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
  room = "defaultRoom"
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
    temperature = str(round((sensehat_temp - ((get_cpu_temp() - sensehat_temp)/2.466)), 2))
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

# read state file/create if doesn't exist yet
states_path = str(room) + "_state.txt"
states_file = Path(states_path)
states_file.touch(exist_ok=True)

sense.clear()
while True:
  with open(states_path, "r") as file:
    AC_State = file.readline().split("=")[1]
    Light_State = file.readline().split("=")[1]

  # display led 
  if Light_State == 1:
    sense.set_pixel(0, 0, (255, 0, 0))
    sense.set_pixel(0, 1, (255, 0, 0))
    sense.set_pixel(0, 2, (255, 0, 0))
    sense.set_pixel(0, 3, (255, 0, 0))
    sense.set_pixel(1, 3, (255, 0, 0))
    sense.set_pixel(2, 3, (255, 0, 0))
  else:
    sense.set_pixel(0, 0, (0, 255, 0))
    sense.set_pixel(0, 1, (0, 255, 0))
    sense.set_pixel(0, 2, (0, 255, 0))
    sense.set_pixel(0, 3, (0, 255, 0))
    sense.set_pixel(1, 3, (0, 255, 0))
    sense.set_pixel(2, 3, (0, 255, 0))

  if AC_State == 1:
    sense.set_pixel(5, 7, (255, 0, 0))
    sense.set_pixel(7, 7, (255, 0, 0))

    sense.set_pixel(5, 6, (255, 0, 0))
    sense.set_pixel(7, 6, (255, 0, 0))

    sense.set_pixel(5, 5, (255, 0, 0))
    sense.set_pixel(7, 5, (255, 0, 0))

    sense.set_pixel(6, 6, (255, 0, 0))
    sense.set_pixel(6, 4, (255, 0, 0))

  else:
    sense.set_pixel(5, 7, (0, 255, 0))
    sense.set_pixel(7, 7, (0, 255, 0))

    sense.set_pixel(5, 6, (0, 255, 0))
    sense.set_pixel(7, 6, (0, 255, 0))

    sense.set_pixel(5, 5, (0, 255, 0))
    sense.set_pixel(7, 5, (0, 255, 0))

    sense.set_pixel(6, 6, (0, 255, 0))
    sense.set_pixel(6, 4, (0, 255, 0))

  sleep(1)

  AC_State_New = 5
  Light_State_New = 5
  for event in sense.stick.get_events(): #on joystick press do action

    # Air-Conditioner TOGGLE
    if event.direction == "up" and event.action == "pressed":
      AC = not AC
      if AC == True:
        AC_State_New = 1
      else:
        AC_State_New = 0  

    # Light TOGGLE
    if event.direction == "down" and event.action == "pressed":
      Light = not Light
      if Light == True:
        Light_State_New = 1
      else:
        Light_State_New = 0
    
    # if any state changed, update state.txt
    if AC_State_New != 5:
      with open(states_path, "w") as file:
        file.writelines("AC_State=" + str(AC_State_New) + "\n")
        file.writelines("Light_State=" + str(Light_State))
    elif Light_State_New != 5:
      with open(states_path, "w") as file:
        file.writelines("AC_State=" + str(AC_State) + "\n")
        file.writelines("Light_State=" + str(Light_State_New))

    # display user action
    print(event.direction, event.action)

    # on release, show all states
    if event.action == "released":
      print("AC State: ", AC_State)
      print("Light State: ", Light_State)

