#Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing the Dataset
Dataset = pd.read_csv("german_credit_data_dataset.csv")
X = Dataset.iloc[:, :-1].values
y = Dataset.iloc[:, [-1]].values


#list all the string value and convert them in to int values!!
#Note we are doing only labelencoder 
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])

X[:, 2] = labelencoder.fit_transform(X[:, 2])

X[:, 3] = labelencoder.fit_transform(X[:, 3])

X[:, 5] = labelencoder.fit_transform(X[:, 5])

X[:, 6] = labelencoder.fit_transform(X[:, 6])

X[:, 8] = labelencoder.fit_transform(X[:, 8])

X[:, 9] = labelencoder.fit_transform(X[:, 9])

X[:, 11] = labelencoder.fit_transform(X[:, 11])

X[:, 13] = labelencoder.fit_transform(X[:, 13])

X[:, 14] = labelencoder.fit_transform(X[:, 14])

X[:, 16] = labelencoder.fit_transform(X[:, 16])

X[:, 18] = labelencoder.fit_transform(X[:, 18])

X[:, 19] = labelencoder.fit_transform(X[:, 19])


#new X values:
print(X)

#feature scale our independent variables 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)



#Splitting the dataset into training and testing set's
from sklearn.model_selection import train_test_split
X_train , X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3, random_state=0, shuffle=True)

#Logistic Regression model. 
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(max_iter=1000, random_state =0, solver='liblinear',multi_class='ovr')
classifier.fit(X_train, y_train)

#predict with test set
y_pred = classifier.predict(X_test)

#evaluating our model.
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
acc_train = accuracy_score(y_train, classifier.predict(X_train))
f1_train = f1_score(y_train, classifier.predict(X_train), average= 'weighted')

print("Traing set results")
print("ACCURACY for train set",acc_train)
print("F1 SCORE for train set",f1_train)

#evaluate with test set
acc_test = accuracy_score(y_test, y_pred)
f1_test = f1_score(y_test, y_pred, average= 'weighted')

print("Test set results")
print("ACCURACY for test set",acc_test)
print("F1 SCORE for test set",f1_test)

#Confusion Matrix 
cm = confusion_matrix(y_test,y_pred)
print(cm)
