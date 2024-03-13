
#Slicing operator

l1 = []

n=int(input("Enter Size of list:"))

print("Enter Data:")

for i in range(0,n):
    l1.append(eval(input()))

print(l1)

sl1 = l1[2::1]
print(sl1)

#we can reverse list by using slicing operator
sl2 = l1[-1::-1]
print(sl2)