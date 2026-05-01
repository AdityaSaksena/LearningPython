entrees = ["beef", "chicken", "tofu", "pork", "fish"]
appetizers = ["salad", "soup", "breadsticks", "nachos", "spring rolls"]
main_dishes = ["steak", "grilled chicken", "stir-fried tofu", "roast pork", "baked fish"]
desserts = ["ice cream", "cake", "pie", "cookies", "pudding"]

response = input("What food do you want to eat? ")
if response in entrees:
    print("That is an entree.")
elif response in appetizers:
    print("That is an appetizer.")
elif response in main_dishes:
    print("That is a main dish.")
elif response in desserts:
    print("That is a dessert.")
else:
    print("That food is not on the menu.")