from time import sleep
from sense_hat import SenseHat
import os
from datetime import datetime
import json
from pathlib import Path

sense = SenseHat()
fan = False
Fan_State = ""
light = False
Light_State = ""

events = {}


def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

def addEvent(date, device, state, temp, humidity):
  global events
  if device == "fan": 
    device_state = "Fan_State"
  if device == "light": 
    device_state = "Light_State"
  #creates file if it doesn't exists
  file = Path('events.json')
  file.touch(exist_ok=True)
  # Open json file
  with open('events.json', "r+") as file:

      # try loading contents as a json dictionary
      try:
          events = json.load(file)
          print("initial json: \n", events)

          # if date variable is not currently inside the keys of the dictionary
          # add new key-value pair and overwrite the json file (additional 2 params are to beautify the json file)
          try:
              if date not in events.keys():
                  events[date] = {device_state : state , "Room_Temperature" : temp, "Room_Humidity" : humidity}
                  print("post json: \n", events)
                  
                  json.dump(events, open('events.json', "w"), indent=2, separators=(',', ': '))

          # something somewhere fucked up
          except:
              print("Something Wrong.")

      # exception occured, likely empty json
      except:
          print("Empty Json File.")
          events = {}
          events[date] = {device_state : state , "Room_Temperature" : temp, "Room_Humidity" : humidity}
          json.dump(events, open('events.json', "w"), indent=2, separators=(',', ': '))
      
      # close the file
      file.close()

sense.clear()
while True:
  sleep(1)
  now = datetime.now()
  formatted_now = now.strftime("%Y/%m/%d-%H:%M:%S")
  # Temperature Data
  temp = sense.get_temperature()
  temp_calibrated = str(round((temp - ((get_cpu_temp() - temp)/2.466)), 2))
  # Humidity Data
  humidity = str(round(sense.get_humidity(),2))

  for event in sense.stick.get_events(): #on joystick press do action
    if event.direction == "up" and event.action == "pressed":
      fan = not fan
      if fan == True:
        Fan_State = "On"
      else:
        Fan_State = "Off"
      addEvent(formatted_now, "fan", Fan_State, temp_calibrated, humidity)  

    if event.direction == "down" and event.action == "pressed":
      fan = not fan
      if fan == True:
        Fan_State = "On"
      else:
        Fan_State = "Off"
      addEvent(formatted_now, "fan", Fan_State, temp_calibrated, humidity) 

    if event.direction == "middle" and event.action == "pressed":
      light = not light
      if light == True:
        Light_State = "On"
      else:
        Light_State = "Off"
      addEvent(formatted_now, "light", Light_State, temp_calibrated, humidity) 
    
    #print(event.direction, event.action)
    if event.action == "released":
      print("Light State: " + Light_State)
      print("Fan State: " + Fan_State)

