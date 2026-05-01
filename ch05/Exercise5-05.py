yes = ["yes", "sure", "okay", "yeah", "yep", "yup", "ok", "k"]
no = ["no", "nope", "nah", "nay", "nuh-uh"]
while True:

    response = input("Should I say Hello, World?: ").lower()
    if response in yes + no:
        break
    else:
        print("Invalid input.")

condition = response in yes

if condition:
    print("Hello, World!")

 

