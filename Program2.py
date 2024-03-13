num = int(input("Enter a Number:"))

first = num%10
num   = num//10

second = num%10
num = num//10

third = num%10
num = num//10

fourth = num%10
num = num//10

Sum = first+second+third+fourth

print("unit: {0},tength: {1},hundredth: {2},thousandth: {3},Sum: {4}".format(first,second,third,fourth,Sum))
