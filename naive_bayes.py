#-------------------------------------------------------------------------
# AUTHOR: Andrew Sanford
# FILENAME: naive_bayes.py
# SPECIFICATION: Problem 5b
# FOR: CS 4210- Assignment #2
# TIME SPENT: 45 Minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

dbTraining = []
dbTesting = []

#reading the training data in a csv file
#--> add your Python code here

with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         dbTraining.append (row)
         #print(row)

with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         dbTesting.append (row)
         #print(row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here

features = {
        "Sunny": 1,
        "Overcast": 2,
        "Rain": 3,
        "Cool": 1,
        "Mild": 2,
        "Hot": 3,
        "Normal": 1,
        "High": 2,
        "Strong": 1,
        "Weak": 2,
    }

X = []

for i in range(len(dbTraining)):
    X.append([])
    X[i].append(features[dbTraining[i][1]])
    X[i].append(features[dbTraining[i][2]])
    X[i].append(features[dbTraining[i][3]])
    X[i].append(features[dbTraining[i][4]])

Z = []

for i in range(len(dbTesting)):
    Z.append([])
    Z[i].append(features[dbTesting[i][1]])
    Z[i].append(features[dbTesting[i][2]])
    Z[i].append(features[dbTesting[i][3]])
    Z[i].append(features[dbTesting[i][4]])

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []

for i in range(len(dbTraining)):
    if dbTraining[i][5] == "Yes":
        Y.append(1)
    else:
        Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here

#printing the header os the solution
#--> add your Python code here
print('%-12s%-12s%-12s%-12s%-12s%-12s%-12s' % ('Day', 'Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis', 'Confidence'))

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here

for i in range(len(Z)):
    prediction = clf.predict_proba([Z[i]])[0]
    if prediction[0] >= 0.75:
        print('%-12s%-12s%-12s%-12s%-12s%-12s%-12s' % (dbTesting[i][0], dbTesting[i][1], dbTesting[i][2], dbTesting[i][3], dbTesting[i][4], 'Yes', str(prediction[0])))
    elif prediction[1] >= 0.75:
        print('%-12s%-12s%-12s%-12s%-12s%-12s%-12s' % (dbTesting[i][0], dbTesting[i][1], dbTesting[i][2], dbTesting[i][3], dbTesting[i][4], 'No', str(prediction[1])))


