"""
*
* *
* * *
* * * *
"""

r = int(input("Enter a rows number:"))
c = int(input("Enter Column number;")) 

for i in range(r):
    for j in range(c):
        if i >= j:
            print("*",end='')
    print()