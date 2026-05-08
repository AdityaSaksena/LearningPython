rivers={}
rivers["nile"] = "egypt"
rivers["amazon"] = "brazil"
rivers["yangtze"] = "china"

for river in rivers:
    print("The", river.title(), "runs through", rivers[river].title())