import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

detaset = pd.read_csv('weather.csv')
# print (detaset.head(10))

# remove class label form columns
x = detaset.drop('class',axis=1)
y = detaset['class']
# print (y)
# print (x)

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)

print ('############################')
print ('dataset train : ')

print(x_train)

print ('############################')
print ('dataset test : ')

print(x_test)

# print('x_train: '+len(x_train))
# print('x_test: '+len(x_test))

