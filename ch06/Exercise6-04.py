favfood = {}
for i in range(5):
    name = input("What is your name? ")
    food = input("What is your favorite food? ")
    favfood[name] = food

for name in favfood:
    print(name+"'s favorite food is", favfood[name])

print("People like:", ", ".join(list(set(favfood.values()))[0:-1]) + ", and " + list(set(favfood.values()))[-1])