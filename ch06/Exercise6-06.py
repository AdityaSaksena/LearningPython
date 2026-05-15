numbers = {}

numbers["zero"] = 0
numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3
numbers["four"] = 4
numbers["five"] = 5
numbers["six"] = 6
numbers["seven"] = 7
numbers["eight"] = 8
numbers["nine"] = 9
numbers["ten"] = 10
numbers["eleven"] = 11
numbers["twelve"] = 12
numbers["thirteen"] = 13
numbers["fourteen"] = 14
numbers["fifteen"] = 15
numbers["sixteen"] = 16
numbers["seventeen"] = 17
numbers["eighteen"] = 18
numbers["nineteen"] = 19

numbers["twenty"] = 20
numbers["thirty"] = 30
numbers["forty"] = 40
numbers["fifty"] = 50
numbers["sixty"] = 60
numbers["seventy"] = 70
numbers["eighty"] = 80
numbers["ninety"] = 90
numbers["hundred"] = 100

inputnum = input("Type out a number: ")

num = inputnum.split("-")

if inputnum in numbers:
    print("The number you typed out is " + str(numbers[inputnum]))
else:
    print("The number you typed out is " + str(numbers[num[0]] + numbers[num[1]]))