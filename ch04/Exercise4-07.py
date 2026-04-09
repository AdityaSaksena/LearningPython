day =input("Enter the day: ")
month = input("Enter the month: ")
year = input("Enter the year: ")
ordinal = ["", "st", "nd", "rd"]
ordinal+=17*["th"]
ordinal+=["st", "nd", "rd"]
ordinal+=7*["th"]
ordinal+=["st"]
months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(f"The date is: {months[int(month)]}, the {day}{ordinal[int(day)]}, {year}")