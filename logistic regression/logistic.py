import pandas as pd
import numpy as np

xtrain = pd.read_csv('Training Data/Logistic_X_Train.csv')
ytrain = pd.read_csv('Training Data/Logistic_Y_Train.csv')

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(xtrain,ytrain)

xtest = pd.read_csv('Test Cases/Logistic_X_Test.csv')
sample_output = pd.read_csv('Test Cases/SampleOutput.csv')
ypred = model.predict(xtest)

import matplotlib.pyplot as plt
plt.scatter(ypred, sample_output[:len(ypred)])
plt.plot(ypred, sample_output[:len(ypred)])
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend(['Predicted', 'Sample Output'])
plt.show()

from sklearn.metrics import r2_score,mean_absolute_error

score1 = r2_score(sample_output[:len(ypred)], ypred)
score2 = mean_absolute_error(sample_output[:len(ypred)], ypred)

print(score1,score2)