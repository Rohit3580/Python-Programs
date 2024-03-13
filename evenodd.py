
def check(ino):
    if ((ino % 2) == 0):
        print(ino,"is even number.")
    else:
        {
            print(ino,"is odd number.")
        }

if __name__ == "__main__":
    inum = int(input("enter number:"))
    check(inum)
