from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as reg

import numpy as np

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

#instantiate the linear model
linear = reg.LinearRegression()
linear.fit(X_train, y_train)
linear_score = linear.score(X_test, y_test)
print(linear_score)


ridge = reg.RidgeRegression()
ridge.set_params(alpha = '0.5')
ridge.fit(X_train, y_train)
ridge_score = ridge.score(X_test, y_test)

alpha = 0.5
models = [model1(alpha), model2(alpha)]

for model in models:
    model.fit(X_train, y_train);




