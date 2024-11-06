import pandas as pd
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
import os

df = pd.read_csv(r'C:\Users\admin\Downloads\mlops\data\raw\df.csv')
df.dropna(inplace=True)
df['workclass'] = df['workclass'].str.replace('?','Not Spe')
#os.mkdir('data/processed')
le = LabelEncoder()


for i in df.columns:
    if df[i].dtype=='object':
        if i=='y':
            df[i] = df[i]
        else:
            df[i] = le.fit_transform(df[i])

df['y'] = df['y'].str.replace('.','')

x = df.drop('y',axis=1)
y = df['y']

x,y = SMOTE().fit_resample(x,y)

x.to_csv(r'C:\Users\admin\Downloads\mlops\data\processed\x.csv',index=False)
y.to_csv(r'C:\Users\admin\Downloads\mlops\data\processed\y.csv',index=False)