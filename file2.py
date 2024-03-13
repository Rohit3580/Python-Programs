# readline(), readlines(), seek()

f1 = open("Demo.txt")

print(f1.readline())             #only read one line at time

print("--------------------------------------")

f1.seek(0)
print(f1.readlines())
f1.close()

print("----------------------------------------")

f1 = open("Demo.txt","r")

lines = f1.readlines()

for i in range(0, len(lines),2):
    print(lines[i].strip())