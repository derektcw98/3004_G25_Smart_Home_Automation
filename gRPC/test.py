import json
import os


client_log_path = os.getcwd() + "\gRPC\client_log.json"























# with open(client_log_path, "r+") as file:
#     # load json object into dictionary
#     try:
#         client_log_json = json.load(file)
#         print(client_log_json)

#         try:
#             date = "2022/07/20-17:11:41"
#             if date not in client_log_json.keys():
#                 client_log_json[date] = {"Fan_State": "OFF","Room_Temperature": 26.8,"Room_Humidity": 49.3}
#                 print(client_log_json)
                
#                 json.dump(client_log_json, open(client_log_path, "w"), indent=2, separators=(',', ': '))
#         except:
#             print("Something Wong.")

#     except:
#         print("Empty Json File.")
#         json.dump({}, open(client_log_path, "w"), indent=2, separators=(',', ': '))
#     file.close()



# xz way modified

# # Open json file
# with open('events.json', "r+") as file:

#     # try loading contents as a json dictionary
#     try:
#         events = json.load(file)
#         print("initial json: \n", events)

#         # if date variable is not currently inside the keys of the dictionary
#         # add new key-value pair and overwrite the json file (additional 2 params are to beautify the json file)
#         try:
#             if date not in events.keys():
#                 events[date] = {device_state : state , "Room_Temperature" : temp, "Room_Humidity" : humidity}
#                 print("post json: \n", events)
                
#                 json.dump(events, open('events.json', "w"), indent=2, separators=(',', ': '))

#         # something somewhere fucked up
#         except:
#             print("Something Wong.")

#     # exception occured, likely empty json
#     except:
#         print("Empty Json File.")
    
#     # close the file
#     file.close()



 
 