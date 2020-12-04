import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer


# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

db = sqlite3.connect('regression.sqlite') # Create a connection to the database
cursor = db.cursor() # https://www.python.org/dev/peps/pep-0249/#cursor-objects

cursor.execute('''CREATE TABLE model_params (
               id INTEGER PRIMARY KEY NOT NULL, 
               desc TEXT, 
               param_name TEXT, 
               value INTEGER)''')


cursor.execute('''CREATE TABLE model_coefs (
               id INTEGER PRIMARY KEY NOT NULL, 
               desc TEXT, 
               feature_name TEXT, 
               value INTEGER)''')


cursor.execute('''CREATE TABLE model_results (
               id INTEGER PRIMARY KEY NOT NULL, 
               desc TEXT, 
               train_score REAL, 
               text_score REAL)''')
