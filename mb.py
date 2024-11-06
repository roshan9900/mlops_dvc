from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import os
import pickle



x = pd.read_csv(r'C:\Users\admin\Downloads\mlops\data\processed\x.csv')
y = pd.read_csv(r'C:\Users\admin\Downloads\mlops\data\processed\y.csv')

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.3, random_state=42)

rf = RandomForestClassifier()
rf.fit(x_train, y_train)

model = pickle.dump(rf, open('model.pkl','wb'))
pred = rf.predict(x_test)

print(classification_report(y_test, pred))

