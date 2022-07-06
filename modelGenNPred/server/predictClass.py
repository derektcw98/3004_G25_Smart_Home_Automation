import pandas as pd
from joblib import load
from io import StringIO
from pathlib import Path
import os

def predictClass(roomName, dataToPredict):

    # Read data from parameter
    df = pd.read_csv(StringIO(dataToPredict), header=None, sep=",")
    df.columns = ["day", "hour", "minute", "temperature", "humidity", "light_state", "aircon_state", "aircon_temp", "room", "label"]

    # tentatively reduced to 5 features for POC
    X = df
    X = X.drop('light_state', axis = 1)
    X = X.drop('aircon_state', axis = 1)
    X = X.drop('aircon_temp', axis = 1)
    X = X.drop('room', axis = 1)
    X = X.drop('label', axis = 1)

    # To predict on edge device
    # load the model from disk
    cwd = Path(os.getcwd())    
    model_path = str(cwd.parent.absolute())+"\\sharedDirectory\\"+roomName+"_knnPrediction.joblib"

    loaded_model = load(open(model_path, 'rb')) #knnPrediction can be replaced with newer model
    result = loaded_model.predict(X)#[[6,9,50,21,23.68,0,0,24]] this is one data
    nearest = loaded_model.kneighbors(X)[1] #returns index of neighbors

    print("Prediction result: ", result)

    # get original csv that model generated from
    csv_path = str(cwd.parent.absolute())+"\\sharedDirectory\\"+roomName+"_training_data.csv"
    checkTempData = pd.read_csv(csv_path, header= None)
    checkTempData.columns = ["day", "hour", "minute", "temperature", "humidity", "light_state", "aircon_state", "aircon_temp", "room"]
    dataForTemp = checkTempData
    dataForTemp = dataForTemp.drop('day', axis = 1)
    dataForTemp = dataForTemp.drop('hour', axis = 1)
    dataForTemp = dataForTemp.drop('minute', axis = 1)
    dataForTemp = dataForTemp.drop('temperature', axis = 1)
    dataForTemp = dataForTemp.drop('humidity', axis = 1)
    dataForTemp = dataForTemp.drop('light_state', axis = 1)
    dataForTemp = dataForTemp.drop('aircon_state', axis = 1)
    dataForTemp = dataForTemp.drop('room', axis = 1)

    # Get average temp
    temp = 0
    count = 0
    for i in nearest[0]:
        count += 1
        temp += dataForTemp.iloc[i]["aircon_temp"]
    avgTemp = (int(round((temp/count),0)))
    print("Average Temperature for AC: ", avgTemp)

    # return predicted class and temperature to server
    return(str(result) + "," + str(avgTemp))