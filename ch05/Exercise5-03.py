number = int(input("Enter a number: "))
if number < 2:
     print(f"{number} is not a prime number.")
else: 
    for denominator in range(1, int(number**0.5) + 1,2):
        if denominator == 1:
            denominator = 2
        if number % denominator == 0:
            print(f"{number} is not a prime number.")
            break
    else: 
        print(f"{number} is a prime number.")