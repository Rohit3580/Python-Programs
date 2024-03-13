
Data={}

for i in range(3):
    code = int(input("Enter code:"))
    price = int(input("Enter price:"))
    Data[code]=price

print(Data)

t1 = tuple(Data.keys())
print(t1)

t2 = tuple(Data.values())
print(t2)