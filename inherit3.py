
#best exampl

class RBI:
    ROI = 7.5
    def Display(self):
        print("Submit Pancard and Aaddharcard Compulsory")

class SBI(RBI):
    Intrest = 5.5
    def Display1(self):
        print("Minimum account balance 500.")

obj1 = SBI()
print("ROI(Rate of Intrest):",obj1.ROI)
print("Rules:",obj1.Display(),obj1.Display1())


