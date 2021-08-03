import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('2020_travel_survey.csv')

train, test = train_test_split(df, test_size=0.33, random_state=42)
target = 'S_Month'
features = df.columns.drop(['ID', target])

X_train = train[features]
y_train = train[target]
X_test = test[features]
y_test = test[target]


Regress = RandomForestClassifier(n_estimators=300, max_leaf_nodes=12)
Regress.fit(X_train, y_train)


pickle.dump(Regress, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[20, 0, 1000, 0]]))