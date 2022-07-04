import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from joblib import dump
from datetime import datetime
from time import sleep

def generateModel():
    #Read data from CSV generated from databbase here
    df = pd.read_csv('noclass.csv')

    labels = []

    #Create class based on device states
    for i in df.index:
        lightState = int(df.iloc[i,5])
        airconState = int(df.iloc[i,6])
        if airconState == 0 and lightState == 0:
            label = "nanl"
        elif airconState == 0 and lightState == 1:
            label = "nagl"
        elif airconState == 1 and lightState == 0: 
            label = "ganl"
        elif airconState == 1 and lightState == 1:
            label = "gagl"
        labels.append(label)

    df.insert(9,"class", labels, True)

    #Add in column names
    #day of week, time, temperature, humidity, light on/off, aircon on/off, aircon temp, room, class
    df.columns = ["day", "hour", "minute", "temperature", "humidity", "light_state", "aircon_state", "aircon_temp", "room", "class"]


    # tentatively reduced to 5 features for POC
    y = df['class']

    #Reduce features
    X = df.drop('class', axis =1)
    X = X.drop('light_state', axis = 1)
    X = X.drop('aircon_state', axis = 1)
    X = X.drop('aircon_temp', axis = 1)
    X = X.drop('room', axis = 1)

    #Split into test and training set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=100)

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
    while accuracy <= (0.98* targetAccuracy): #adjust multiplier accordingly
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
    knnPickle = open('knnPrediction', 'wb') 

    classifier = KNeighborsClassifier(n_neighbors=n)
    classifier.fit(X_train, y_train)

    # source, destination 
    dump(classifier, 'knnPrediction.joblib')  
    knnPickle.close()
    print("Model Saved")
    # #To predict on edge device
    # # load the model from disk
    # loaded_model = pickle.load(open('knnPrediction', 'rb'))
    # result = loaded_model.predict(X_test)
    # print(result)

while True:
    now = datetime.now()
    dayOfWeek = now.weekday()
    print(dayOfWeek)
    if dayOfWeek == 6:
        print("generating model")
        generateModel()
    print("Awaiting next day...")
    sleep(60*60*24)