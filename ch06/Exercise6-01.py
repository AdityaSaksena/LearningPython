price = {}
price["apple"] = 1.5
price["banana"] = 2
price["orange"] =  2.5
item = input("What do you want to buy? ")
if item in price:
    print("The price of", item, "is", price[item])
else:    
    print("Sorry, we don't have", item)