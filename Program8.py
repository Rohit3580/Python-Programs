
#tuple

t1 = 1,"hello",8.9,7+5j

print(t1)
print(t1[3])

t2 = (1,"abc",3.14,[4,5,6],'true')

print(t2[0])

print(t2[3])                                # output = 4,5,6

print(t2[3][0])                            # 4

print(t2[3][2])                            #6

print(t2[4])                               #true

print("Length of t1: ",len(t1))
print("Length of t2: ",len(t2))
print("Length of t2[3]:",len(t2[3]))