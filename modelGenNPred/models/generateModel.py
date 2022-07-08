import pathlib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from joblib import dump
from datetime import datetime
from time import sleep
from pathlib import Path
import os

def generateModel(room,dataframe):
    #Read data from dataframe passed in
    df = dataframe

    ## Label generation done on client instead ##
    # labels = []
    
    # Add in column names
    # day of week, time, temperature, humidity, light on/off, aircon on/off, aircon temp, room, label
    df.columns = ["day", "hour", "minute", "temperature", "humidity", "aircon_temp", "room", "label"]


    # tentatively reduced to 5 features for POC
    y = df['label']

    #Reduce features
    X = df.drop('label', axis =1)
    X = X.drop('aircon_temp', axis = 1)
    X = X.drop('room', axis = 1)

    #Split into test and training set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    # Generate model for exporting
    n = 5
    knn = KNeighborsClassifier(n_neighbors=n)
    knn.fit(X_train, y_train)
    Y_predTrain = knn.predict(X_train)
    Y_predTest = knn.predict(X_test)
    targetAccuracy = accuracy_score(y_train, Y_predTrain)
    accuracy = accuracy_score(y_test, Y_predTest)
    print("Target Accuracy: " + str(round(targetAccuracy,4)),"Accuracy: " + str(round(accuracy,4)))

    #if accuracy less than 98% of training accuracyy, add neighbours
    while accuracy <= (0.975* targetAccuracy): #adjust multiplier accordingly
        n += 2
        classifier = KNeighborsClassifier(n_neighbors=n)
        classifier.fit(X_train, y_train)
        Y_predTrain = classifier.predict(X_train)
        Y_predTest = classifier.predict(X_test)
        accuracy = accuracy_score(y_test, Y_predTest)
        print("Number of neighbours: " + str(n))
        print("Target Accuracy: " + str(round(targetAccuracy,4)),"Accuracy: " + str(round(accuracy,4)), "Percent: " + str(round((accuracy/targetAccuracy),4)))
    else:
        print("Target Accuracy Reached")

    #Create model to export
    classifier = KNeighborsClassifier(n_neighbors=n)
    classifier.fit(X_train, y_train)

    # source, destination 
    cwd = Path(os.getcwd())    
    model_path = str(cwd.parent.absolute())+"\\sharedDirectory\\"+room+"_knnPrediction.joblib"
    model_path = Path(model_path)
    dump(classifier, model_path)  
    print("Model Saved")
    # #To predict on edge device
    # # load the model from disk
    # loaded_model = pickle.load(open('knnPrediction', 'rb'))
    # result = loaded_model.predict(X_test)
    # print(result)
