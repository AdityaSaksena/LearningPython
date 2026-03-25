elephantbodyparts=[]
for n in range(3):
    bodyparts=input("Enter one body part of an elephant: ")
    elephantbodyparts.append(bodyparts)
elephantbodyparts[-1]="and "+elephantbodyparts[-1]
print("The elephant has these body parts:", ", ".join(elephantbodyparts))
