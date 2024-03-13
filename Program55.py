"""
1 2 3 4 
5 6 7 8 
9 1 2 3
4 5 6 7
"""
r = int(input("Enter row number:"))
c = int(input("Enter Column number:"))

k = 1
for i in range(r):
    for j in range(c):
        if k <= 9:
            print(k,end='')
        else:
            k = 1
            print(k,end='')
        k = k+1
    print()
        