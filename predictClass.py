import pickle
import pandas as pd


#Read data from CSV generated from databbase here
df = pd.read_csv('noclass.csv')
df.columns = ["day", "hour", "minute", "temperature", "humidity", "light_state", "aircon_state", "aircon_temp", "room"]

df.insert(9,"class", True)

# tentatively reduced to 5 features for POC
y = df['class']
X = df.drop('class', axis =1)
X = X.drop('light_state', axis = 1)
X = X.drop('aircon_state', axis = 1)
X = X.drop('aircon_temp', axis = 1)
X = X.drop('room', axis = 1)

#To predict on edge device
# load the model from disk
loaded_model = pickle.load(open('knnPrediction', 'rb'))
result = loaded_model.predict([[3,23,10,20.0,60]])
print(result)