friendsages = []
for n in range(5):
    friendsages.append(int(input("Enter a friend's age: ")))
    
print("The youngest friend is:", min(friendsages))
print("The oldest friend is:", max(friendsages))