# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 20:52:43 2021

@author: Swaminathan ayyappan
"""


import pandas as pd #Importing pandas
import pickle #Importing pickle 
df = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/crop_recommendation/train_set_label.csv") #Reading the dataframe using pandas

X=df.iloc[:,0:7].values #Indepent features converted into an numpy array.
y=df.iloc[:,7].values #Dependent features converted into an numpy array.

from sklearn.preprocessing import LabelEncoder #Importing labelencoder from scikit learn.
le=LabelEncoder() #Instantiating the labelencoder class.

y=le.fit_transform(y) #Encoding the dependent features into numerical form with the use of label encoder.

from sklearn.model_selection import train_test_split #Importing train and test split from sklearn.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101) #Performing train test split with test size of 20% and random state as 101

#Naive bayes classification model
#The reason for using naive bayes algorithm is it deals in predicting output class which has more than two features based upon the probability calculated using baye's theorem.
from sklearn.naive_bayes import GaussianNB #Importing Naive bayes from sklearn.
nb_classifier=GaussianNB() #Instantiating the naive bayes classifier class.

#Model training
nb_classifier.fit(X_train,y_train) #training the model with the training data.

# Saving model into an bytecode format
pickle.dump(nb_classifier, open('C:\\Users\\swaminathan.ayyappan\\Desktop\\docker-test\\Crop-recommendation-using-ML-ETE-Deployment\\Code\\Croprecommendationmodel.pkl','wb'))
