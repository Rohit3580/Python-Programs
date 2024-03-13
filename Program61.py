
try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number"))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Thank you....")