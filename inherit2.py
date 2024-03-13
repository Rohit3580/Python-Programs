#inhetiance and super() method 

class Parent:
    def __init__(self,ino):
        self.x = ino
        print(self.x)


class Child(Parent):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y

obj1 = Child(10,20)

print("Value of y:",obj1.y)
print("Value of x:",obj1.x)
