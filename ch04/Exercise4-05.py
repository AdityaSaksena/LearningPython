ourfavoritefoods = []
for n in range(4):
    food=input("Enter a food you and your friend like: ")
    ourfavoritefoods.append(food)
myfavoritefoods = ourfavoritefoods[:]
myfriendsfavoritefoods = ourfavoritefoods[:]
print("Our favorite foods are:", ourfavoritefoods)
myfavoritefoods.append(input("What is a food you also like?"))
myfriendsfavoritefoods.append(input("What is a food your friend also likes?"))

myfavoritefoods[-1]="and "+myfavoritefoods[-1]
myfriendsfavoritefoods[-1]="and "+myfriendsfavoritefoods[-1]

print("I like these foods", ", ".join(myfavoritefoods))
print("My friend likes these foods", ", ".join(myfriendsfavoritefoods))

#I like foods like pizza, burger, soda, candy, and fries