import os
import sklearn
import numpy as np
import pandas as pd
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree, metrics
from sklearn.model_selection import train_test_split


data = pd.read_csv('pima.csv',names=['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label'])

data.head()
data['label'],label_names = pd.factorize(data['label'])

print(label_names)
print(data['label'].unique())

data['pregnant'],_ = pd.factorize(data['pregnant'])
data['glucose'],_ = pd.factorize(data['glucose'])
data['bp'],_ = pd.factorize(data['bp'])
data['skin'],_ = pd.factorize(data['skin'])
data['insulin'],_ = pd.factorize(data['insulin'])
data['bmi'],_ = pd.factorize(data['bmi'])
data['pedigree'] = pd.factorize(data['pedigree'])
data['age'] = pd.factorize(data['age'])
data.head()

X = data.iloc[:,:-1]
y = data.iloc[:,-1]
# split data randomly into 80% training and 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# train the decision tree
dtree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
dtree.fit(X_train, y_train)

# use the model to make predictions with the test data
y_pred = dtree.predict(X_test)
# how did our model perform?
count_misclassified = (y_test != y_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
accuracy = metrics.accuracy_score(y_test, y_pred)
print('Accuracy: {:.2f}'.format(accuracy))
