# -*- coding: utf-8 -*-
"""Heart Failure Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JkOJ1YyLeYmuhFP2_Vd6l7tTBeVbgE6m
"""

#from google.colab import files
#uploaded = files.upload()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
#hf = pd.read_csv(io.BytesIO(uploaded['heart_failure_clinical_records_dataset.csv']))
url='https://raw.githubusercontent.com/ridwane369/heart_failure_clinical_records_dataset/master/heart_failure_clinical_records_dataset.csv'
hf = pd.read_csv(url)

print(type(hf))

print("Keys of hf_dataset:\n", hf.keys())

print("Age:\n",hf['age'])

print("Death Event:\n",hf['DEATH_EVENT'])

hf.head()

X_hf = hf.drop("DEATH_EVENT",axis=1)
X_hf = X_hf.drop("time",axis=1)
X_hf.head()

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_hf)
X_scaled= scaler.transform(X_hf)

print(X_scaled)
print(X_scaled.shape)

y = hf["DEATH_EVENT"].values
print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y , test_size = 0.75, random_state=0)

"""KNN Model:"""

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train,y_train)
knn.score(X_test,y_test)

X_new = np.array([[85, 1, 600, 0, 25, 1, 210000.00, 2.5, 135, 0, 1]])
#print("X_new.shape:", X_new.shape)
#print("X_train.shape", X_test.shape)
prediction = knn.predict(X_new)
print("Prediction_KNN:", prediction)

"""Logistic Regression:"""

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train,y_train)
print("Score")
print(classifier.score(X_test,y_test))

predict = classifier.predict(X_new)
print(predict)

from sklearn.linear_model import LinearRegression
linreg = LinearRegression().fit(X_train, y_train)
print("R-squared score (test):",linreg.score(X_test, y_test))

hfdf = pd.DataFrame(X_train, columns=['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
       'ejection_fraction', 'high_blood_pressure', 'platelets',
       'serum_creatinine', 'serum_sodium', 'sex', 'smoking'])
# create a scatter matrix from the dataframe, color by y_train
pd.plotting.scatter_matrix(hfdf, c=y_train, figsize=(15, 15),
                           marker='o', hist_kwds={'bins': 20}, s=60,
                           alpha=.8)

print(max(hf['age']))

"""Droping some features to see if accuracy increases with KNN and Logistic Regression."""

X_hf_v2=hf.drop(['anaemia',  'diabetes',
        'high_blood_pressure', 
         'sex', 'smoking', 'time',
       'DEATH_EVENT'],axis=1)
print(X_hf_v2.keys())

"""KNN"""

scaler.fit(X_hf_v2)
X_scaled2= scaler.transform(X_hf_v2)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_scaled2, y , test_size = 0.75, random_state=0)
knn2 = KNeighborsClassifier(n_neighbors=4)
knn2.fit(X_train2,y_train2)
knn2.score(X_test2,y_test2)

"""Logistic Regression"""

classifier2 = LogisticRegression(random_state = 0)
classifier2.fit(X_train2,y_train2)
print("Score for LogR")
print(classifier2.score(X_test2,y_test2))