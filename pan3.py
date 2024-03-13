#rows opersation and csv file loading

import pandas as pd

df = pd.read_csv("C:/Users/Rohit/OneDrive/Desktop/employtable.csv")
print(df)
print("1------------------------------------------------")
print(df.loc[2]) #display single row
print("2------------------------------------------------")
print(df.loc[[0,1]])   #display multiple rows
print("3------------------------------------------------")
df.loc[4,'e_id'] = 105   #updating values
print(df)
print("4------------------------------------------------")
df.loc[5] = [106,'James',15111,'Jalgaon']  #Add new row
print(df)
print("5------------------------------------------------")
df = df.drop(5)    #delete row
print(df)