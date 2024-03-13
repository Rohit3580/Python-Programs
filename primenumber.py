
def checkprime(ino):
    inum = ino
    icount = 0
    for i in range(2,ino):
        if ((inum % i) == 0):
            icount = icount + 1
            break

    if(icount > 0):
        print(inum,"is not prime number.")
    else:
        print(inum,"is a prime number.")

if __name__ == "__main__":
    iNo = int(input("Enter a number:"))
    checkprime(iNo)