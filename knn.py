#-------------------------------------------------------------------------
# AUTHOR: Andrew Sanford
# FILENAME: knn.py
# SPECIFICATION: Problem 3e
# FOR: CS 4210- Assignment #2
# TIME SPENT: 30 Minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
incorrect_predictions = 0

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#loop your data to allow each instance to be your test set
for i in range(len(db)):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    X = []

    for j in range(len(db)):
        if j != i:
            X.append([int(db[j][0]), int(db[j][1])])

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    Y = []

    for j in range(len(db)):
        if j != i:
            if db[j][2] == '-':
                Y.append(1)
            else:
                Y.append(2)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = [int(db[i][0]), int(db[i][1])]

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if class_predicted == 1 and db[i][2] == '+':
        incorrect_predictions += 1
    elif class_predicted == 2 and db[i][2] == '-':
        incorrect_predictions += 1

#print the error rate
#--> add your Python code here
print("Error rate: " + str(incorrect_predictions / len(db)))






