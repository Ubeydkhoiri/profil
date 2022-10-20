# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier

# Load dataset titanic
titanic = sns.load_dataset('titanic')

# Drop columns 'class','who','adult_male', 'deck', 'embarked','embark_town','alone','alive'
titanic = titanic.drop(['class','who','adult_male', 'deck', 'embarked','embark_town','alone','alive'], axis=1)
titanic['age'] = titanic['age'].fillna(titanic['age'].median())

# Dictionary containing the mapping
variety_mappings = {0: 'Meninggal', 1: 'Selamat'}

# Encoding the target variables to integers
titanic['sex'] = [1 if i == 'male' else 0 for i in titanic['sex']]


X = titanic.drop('survived', axis=1)  # Extracting the independent variables
y = titanic['survived']  # Extracting the target/dependent variable


# Modelling
model_dt = DecisionTreeClassifier()
model_dt.fit(X, y)

def classify(a, b, c, d, e, f):
    arr = np.array([a, b, c, d, e, f]) # Convert to numpy array
    arr = arr.astype(np.float64) # Change the data type to float
    query = arr.reshape(1, -1) # Reshape the array
    prediction = variety_mappings[model_dt.predict(query)[0]] # Retrieve from dictionary
    return prediction # Return the prediction