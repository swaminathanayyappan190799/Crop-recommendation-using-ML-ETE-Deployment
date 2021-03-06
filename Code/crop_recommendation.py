# -*- coding: utf-8 -*-
"""Crop Recommendation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZihwJ_GVbGYKaYr2dxSJnFI0rvDR_MM8

# Crop Recommendation using Machine Learning

Prepared by : Swaminathan ayyappan

Email : swamynathanayyappan@gmail.com

LinkedIn : https://www.linkedin.com/in/swaminathan-ayyappan-60b685175/

Problem Description :

  Provided an input data which contains of features like N,P,K,temperature,humididty,ph,rainfall and crop.And their Description is given below :


  
  N - ratio of Nitrogen content in soil
  
  P - ratio of Phosphorus content in soil
  
  K - ratio of Potassium content in soil
  
  temperature - temperature in degree Celsius
  
  humidity - relative humidity in %
  
  ph - ph value of the soil
  
  rainfall - rainfall in mm
  
  crop - Suitable crop to grow (target variable)

So our work is to predict which type of crop should we want to prefer/recommend based on those input features

## **Importing Libraries**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd #Importing pandas
import seaborn as sns #Importing seaborn
import matplotlib.pyplot as plt #Importing matplotlib 
from google.colab import files #Importing files 
# %matplotlib inline 
df=pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/crop_recommendation/train_set_label.csv") #Reading the training data using pandas.

#Reviewing the first five entries in the training data(df).
df.head()

"""# **Exploratory Data Analysis**"""

#Checking for any null values inside the training dataset(df).
df.isna().sum()

#Identifiying how many number of categories present in the crop column of the training dataset(df).
df.crop.nunique()

#Identifying how many times each categories are present in the crop column.
df['crop'].value_counts()

df.describe() #Gives an statistical analysis of the training data.

df.info() #Provides the information about the training data.

df.shape #Gives the number of rows and columns in the training data.

df.corr() #Gives the pearson correlation of each features on the training data.

"""# **Visualization using seaborn**"""

sns.distplot(df['N']) #Verifying distribution of the N column in the training data.

sns.pairplot(df) #Gives an entire visualization chart about the training data.

sns.jointplot('P','rainfall',data=df) #Compares and visualizes the P and rainfall column on the training data.

sns.jointplot('K','rainfall',data=df) #Compares and visualizes the K and rainfall column on the training data.

sns.jointplot('ph','rainfall',data=df) #Compares and visualizes the ph and rainfall column on the training data.

"""# **Dependent and Independent Features Selection**"""

X=df.iloc[:,0:7].values #Indepent features converted into an numpy array.
y=df.iloc[:,7].values #Dependent features converted into an numpy array.

X #Independent features.

y #Dependent features.

"""**Encoding the target variable (crop) on the training data**"""

from sklearn.preprocessing import LabelEncoder #Importing labelencoder from scikit learn.
le=LabelEncoder() #Instantiating the labelencoder class.

y=le.fit_transform(y) #Encoding the dependent features into numerical form with the use of label encoder.

y #Dependent features after performing label encoding.

from collections import Counter #Importing counter from collections.
print(Counter(y)) #Printing the presence of each distinct values on the dependent features.

"""# **Train and test split**"""

from sklearn.model_selection import train_test_split #Importing train and test split from sklearn.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101) #Performing train test split with test size of 20% and random state as 101

"""# **Naive bayes classification model**"""

#The reason for using naive bayes algorithm is it deals in predicting output class which has more than two features based upon the probability calculated using baye's theorem.
from sklearn.naive_bayes import GaussianNB #Importing Naive bayes from sklearn.

nb_classifier=GaussianNB() #Instantiating the naive bayes classifier class.

"""# **Model training**"""

nb_classifier.fit(X_train,y_train) #training the model with the training data.

"""# **Importing Test data**"""

#Importing the test data.
test_data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/crop_recommendation/test_set_label.csv')

test_data=test_data.iloc[:,:].values #Converts the test data into an numpy array.

test_data #test data after converting it into an numpy array.

"""# **Making predictions using the trained model**"""

#making predictions from the trained naive bayes model using the test data.
predictions=nb_classifier.predict(test_data)

predictions #Reviewing the predictions

"""**Converting the predictions into an dataframe using pandas**"""

#Converting the predictions into an pandas dataframe.
predictions=pd.DataFrame(predictions,columns=['prediction'])

#Reviewing the predictions dataframe.
predictions.head()

"""**Decoding the predictions into text**"""

#A function that is used in decoding the predictions from numerical form into character form for understanding of the predictions made by the classifier model.
def conversion(n):
  crop_names={0:'apple',1:'banana',2:'blackgram',3:'chickpea',4:'coconut',5:'coffee',6:'cotton',7:'grapes',8:'jute',9:'kidneybeans',
              10:'lentil',11:'maize',12:'mango',13:'mothbeans',14:'mungbean',15:'muskmelon',16:'orange',17:'papaya',18:'pigeonpeas',19:'pomegranate',20:'rice',21:'watermelon'}
  return crop_names[n]

#Applying the conversion function and converting it into an dataframe.
final_result=pd.DataFrame(predictions['prediction'].apply(conversion))

final_result.head()

"""# **Converting the final predictions dataframe into an csv file**"""

#Converting the predictions dataframe into an csv file and at last downloading the csv file 
final_result.to_csv('Final predictions.csv',index=False)
files.download('Final predictions.csv')#Note : This line of code works only on google colab