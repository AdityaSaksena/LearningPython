age = int(input("What is your age? "))
if 0 <= age < 13:
    print("You are a child.")
if 13 <= age < 20:
    print("You are a teenager.")
if 18 <= age < 65:
    print("You are an adult.")
if age >= 65:
    print("You are a senior.")