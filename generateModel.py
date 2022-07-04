import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
import pickle


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
X = X.drop('minute', axis = 1)
X = X.drop('light_state', axis = 1)
X = X.drop('aircon_state', axis = 1)
X = X.drop('aircon_temp', axis = 1)
X = X.drop('room', axis = 1)
X = X.drop('humidity', axis = 1)

#Split into test and training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

#Generate accuracy score
testNeighbors = [1,3,5,7,9,11,13,15,17,19,21,31,41,51,61,71,81,91,101,201,265]
trainAcc = []
testAcc = []

# Calculating error for K values between 1 and 265
for i in testNeighbors:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    Y_predTrain = knn.predict(X_train)
    Y_predTest = knn.predict(X_test)
    trainAcc.append(accuracy_score(y_train, Y_predTrain))
    testAcc.append(accuracy_score(y_test, Y_predTest))

# Generate model for exporting
n = 5
classifier = KNeighborsClassifier(n_neighbors=n)
classifier.fit(X_train, y_train)
Y_predTrain = knn.predict(X_train)
Y_predTest = knn.predict(X_test)
targetAccuracy = accuracy_score(y_train, Y_predTrain)
accuracy = accuracy_score(y_test, Y_predTest)

#if accuracy less than 98% of training accuracyy, add neighbours
if accuracy <= (0.98* targetAccuracy):
    n += 2
    classifier = KNeighborsClassifier(n_neighbors=n)
    classifier.fit(X_train, y_train)
    Y_predTrain = knn.predict(X_train)
    Y_predTest = knn.predict(X_test)
    accuracy = knn.predict(X_test)
else:
    print(n)

#Create model to export
knnPickle = open('knnPrediction', 'wb') 

# source, destination 
pickle.dump(knn, knnPickle)  
knnPickle.close()
print("Model Saved")

# #To predict on edge device
# # load the model from disk
# loaded_model = pickle.load(open('knnPrediction', 'rb'))
# result = loaded_model.predict(X_test)
# print(result)