

friends = ["Ørjan", "William", "Sander"]
len(friends)
for index in range(len(friends)):
    print (friends[index])          #Will print firends the same order


#for index in range(10):
 #   print (index)       #will print 0-9 (10 numbers)

#for index in range(3, 10):
 #   print (index)       #will print 3-9


for index in range(5):    #will print "first Int. for index nr 0 and then not first the 4 remaining"
    if index == 0:
        print ("first Iteration")
    else:
        print ("Not First")