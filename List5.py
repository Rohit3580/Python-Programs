class Arithmetic:
    def Add(self,lst):
       sum = 0
       for x in lst: 
        sum = sum+x
       return sum

    def Mult(self,lst):
        mult = 1
        for x in lst:
            mult = mult * x
        return mult
    

l1 = []

size = int(input("Enter size of list: "))

print("Enter the elements of list:")
for i in range(size):
    l1.append(int(input()))

print(l1)

obj = Arithmetic()

Ans1 = obj.Add(l1)
print("Addition is:",Ans1)

Ans2 = obj.Mult(l1)
print("Multiplication is:",Ans2)

