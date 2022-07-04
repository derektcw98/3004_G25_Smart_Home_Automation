import pandas as pd
from joblib import load
#

#Read data from CSV generated from databbase here
df = pd.read_csv('toPredict.csv', header= None)
df.columns = ["day", "hour", "minute", "temperature", "humidity", "light_state", "aircon_state", "aircon_temp", "room"]

# tentatively reduced to 5 features for POC
X = df
X = X.drop('light_state', axis = 1)
X = X.drop('aircon_state', axis = 1)
X = X.drop('aircon_temp', axis = 1)
X = X.drop('room', axis = 1)

#To predict on edge device
# load the model from disk
loaded_model = load(open('D:/Git Repos/3004_G25_Smart_Home_Automation/knnPrediction.joblib', 'rb')) #knnPrediction can be replaced with newer model
result = loaded_model.predict(X)#[[6,9,50,21,23.68,0,0,24]] this is one data

#replace with a command to trigger actuator/ update state
print(result)