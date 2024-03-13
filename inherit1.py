#inheritance

class Parent:
    x = 5
    def Fun(self):
        print("Inside Fun")


class Child(Parent):
    y = 10
    def Gun(self):
        print("Inside Gun..")



obj1 = Child()
print("Value of y:",obj1.y)
print(obj1.Gun())
print("-------------------")
print("Value of x:",obj1.x)
print(obj1.Fun())