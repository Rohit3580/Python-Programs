"""
* * * *
* * * *
* * * *
* * * *
"""

r = int(input("Enter a row number:"))
c = int(input("Enter Column number:"))

for i in range(r):
    for j in range(c):
        print("*",end='')
    print()