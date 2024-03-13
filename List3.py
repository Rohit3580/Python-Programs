#Checking inbuild functions

lst = []

size = int(input("Enter size of list:"))

print("Enter the elements of list:")
for i in range(size):
    lst.append(int(input()))

print(lst)

lst.sort()
print("Sorted list is:",lst)

lst.reverse()
print("Reverse list is:",lst)

x = lst.pop(1)
print("Pop element is:",x)