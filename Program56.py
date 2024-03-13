#prime number program

def checkprime(no):
    flag = False
    for i in range(2,no):
        if no % i == 0:
            flag = True
            break

    return flag
        

n = int(input("Enter Number:"))
ans = checkprime(n)
if ans == True:
    print("Number is not prime")
else:
    print("Number is prime")
