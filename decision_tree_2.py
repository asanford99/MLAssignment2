#-------------------------------------------------------------------------
# AUTHOR: Andrew Sanford
# FILENAME: decision_tree_2.py
# SPECIFICATION: Problem 2
# FOR: CS 4210- Assignment #2
# TIME SPENT: 45 Minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
dbTesting=[]
data = []
dataClass = []

features = {
        "Young": 1,
        "Prepresbyopic": 2,
        "Presbyopic": 3,
        "Myope": 1,
        "Hypermetrope": 2,
        "Yes": 1,
        "No": 2,
        "Reduced": 1,
        "Normal": 2,
    }

with open('contact_lens_test.csv', 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTesting.append (row)

for i in range(len(dbTesting)):
    data.append([])
    data[i].append(features[dbTesting[i][0]])
    data[i].append(features[dbTesting[i][1]])
    data[i].append(features[dbTesting[i][2]])
    data[i].append(features[dbTesting[i][3]])

for i in range(len(dbTesting)):
        if dbTesting[i][4] == "Yes":
            dataClass.append(1)
        else:
            dataClass.append(2)

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    accurate_predictions = 0

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here 

    X = []

    for i in range(len(dbTraining)):
        X.append([])
        X[i].append(features[dbTraining[i][0]])
        X[i].append(features[dbTraining[i][1]])
        X[i].append(features[dbTraining[i][2]])
        X[i].append(features[dbTraining[i][3]])

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    Y = []

    for i in range(len(dbTraining)):
        if dbTraining[i][4] == "Yes":
            Y.append(1)
        else:
            Y.append(2)

    #loop your training and test tasks 10 times here
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here

       for i in range(len(data)):
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here

           class_predicted = clf.predict([data[i]])[0]      

           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here
           if class_predicted == dataClass[i]:
               accurate_predictions += 1
    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    average_accuracy = accurate_predictions / (10 * len(dbTesting))

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("Final accuracy when training on " + ds + ": " + str(average_accuracy))




