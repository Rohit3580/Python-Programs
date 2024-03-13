
def Addition(*k):
    sum = 0
    for i in k:
        sum = sum + i

    print(sum)

print("Enter Data")
t1 = tuple([int(i) for i in input().split(' ')]) 
Addition(*t1)
