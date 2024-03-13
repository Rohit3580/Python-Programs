#columns operation

import pandas as pd


data = ([1001,'Virat',25000,'Pune'],[1002,'Rohit',20000,'Nagpur'],
        [1003,'Shri',21000,'Hydrabad'],[1004,'Rahul',22000,'Bangolre'],
        [1005,'Shubh',15000,'Delhi'],[1006,'Rajat',16000,'Mumbai'])

df = pd.DataFrame(data, columns=['emp_id','name','salary','city'])
print(df)

print("--------------------------------------------------------------")

print(df['name'])      # select / display single colm

print("--------------------------------------------------------------")

print(df[['name','city']])   #display/select multiple columns

print("--------------------------------------------------------------")

df.insert(4,'phone_no',[10,20,'null',40,50,'null'])   #add new colm at sepecific postion
print(df)

print("--------------------------------------------------------------")

print(df[df['phone_no'] == 'null'])  #finding null values

print("--------------------------------------------------------------")

del df['phone_no']     #delete colm
print(df)
print("--------------------------------------------------------------")

df = df.rename(columns={'name':'ename'})
print(df)



