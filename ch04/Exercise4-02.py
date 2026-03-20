list=[1,3,5,7,9,11,13,15,17,19]
for i in range(len(list)):
    print(list[i])
    list[i]=list[i]**2
print(list)