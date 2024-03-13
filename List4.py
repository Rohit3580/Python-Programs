#Write a Python program to sum all the items in a list.



def Addition(lst):
    sum = 0
    for x in lst: 
        sum = sum+x
   
    return sum


l1 = []

size = int(input("Enter size of list: "))

print("Enter the elements of list:")
for i in range(size):
    l1.append(int(input()))

print(l1)

Ans = Addition(l1)
print("Addition is:",Ans)





    