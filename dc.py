from ucimlrepo import fetch_ucirepo 
import os
  
census_income = fetch_ucirepo(id=20) 
  
X = census_income.data.features 
y = census_income.data.targets 

os.makedirs('data/raw')
X['y'] = y
df = X

df.to_csv(r'C:\Users\admin\Downloads\mlops\data\raw\df.csv',index=False)
