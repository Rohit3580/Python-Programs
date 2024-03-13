#their is predefined function for tuple so covert the tuple into list and then perform operation

print("Enter Data")
t1 = tuple([eval(i) for i in input().split(' ')])       

l1 = list(t1)
print(l1)
