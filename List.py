

friends = ["Sander", "Ørjan", "Torgeir", "William"]

print (friends[1])

print (friends[-3])

print (friends [1:]) # everything after position 1

friends[1] = "Ørjan"
print (friends[1])

lucky_numbers = [3, 9, 13, 27, 420, 1337]
friends.extend(lucky_numbers) # Put lists together
friends.insert (1, "Alex")
friends.remove ("Torgeir")
print ("Friends and Lucky Numbers put together")
print (friends)
print (friends.index("Ørjan"))   
print ("Found Ørjans index = 2")
friends.sort
print(friends)

friends2 = friends.copy()

