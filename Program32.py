# greater number x y z

x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
z=int(input("Enter Third Number:"))

if x>y and x>z:
    print(x,"is greater number.")
elif y>x and y>z:
    print(y,"is greater number.")
else:
    print(z,"is greater number.")