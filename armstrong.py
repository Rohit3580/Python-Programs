
def checkarmstrong(ino):
    inum = ino
    idigit = 0
    isum = 0
    icube = 0

    while(inum != 0):
        idigit = inum % 10
        icube = idigit*idigit*idigit
        isum = icube+isum
        inum = inum//10

    if(ino == isum):
        print(ino,"is armstrong number.")
    else:
        print(ino,"is not armstrong.")

if __name__ == "__main__":
    inumber = int(input("enter 3 digit number:"))
    checkarmstrong(inumber)