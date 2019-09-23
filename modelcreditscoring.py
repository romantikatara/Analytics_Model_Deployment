# Model Credit Scoring dengan Random Forest

'''
Model ini memprediksi apakah orang dengan pendidikan dan usia tertentu serta record terlambat/tidaknya pembayaran pertama kedua dan ketiga dapat diberikan kredit atau tidak 
'''

# Import libraries dan Packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import requests
import json

# Import dataset
dataset = pd.read_csv('dataset.csv')


# Menentukan X dan Y dari dataset yang digunakan
X = dataset.iloc[:,0:5].values
Y = dataset.iloc[:,-1].values

# Membagi X dan Y menjadi train dan test untuk membuat model dan melakukan tes pada model yang dibuat
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30) # Train didapat dari 70% data, test 30% dari data 

# Membuat model credit scoring dengan menggunakan Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
modelrandomforest = RandomForestClassifier()

# Train model dengan train dataset yang dihasilkan dari split dataset
modelrandomforest.fit(X_train,Y_train)
Y_pred=modelrandomforest.predict(X_test)

# Menyimpan model dalam disk (serialization)
pickle.dump(modelrandomforest, open('modelcreditscoring.pkl','wb'))

# Load model untuk membandingkan hasil yang didapat
model = pickle.load(open('modelcreditscoring.pkl','rb'))
print(model.predict([[32, 2, 0, 2, 1]]))
