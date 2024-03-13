# open(), read(), close(), write(), *append [a], r, w


if __name__ == "__main__":
    f1 = open("Demo.txt", "w")
    f1.write("My name is Rohit Arvikar. I am MCA Student.")
    f1.close()

    

    f1 = open("Demo.txt","a")
    f1.write("My college name is DYIMR.")

    f1=open("Demo.txt")
    print(f1.read())
    f1.close()
    

    

   