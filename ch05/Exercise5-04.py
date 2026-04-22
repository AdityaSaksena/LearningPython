number = int(input("Enter a number: "))
if number < 2:
    print("There are no prime numbers less than 2.")
else:
    counter = 0
    for num in range(2, number):
        for denominator in range(2, int(num**0.5) + 1):
            if num % denominator == 0:
                break
        else:
            counter += 1
        if num % 10000 == 0:
            print(num)
    print(f"There are {counter} prime numbers less than {number}.")