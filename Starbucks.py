


print ("Hello and welcome to Starbucks!")

name = input("What is your name?\n ")
print ("Hello " + name + "thanks for coming to Starbucks today. \n\n\n")

menu = "Black Coffee, Hot Chocolate, Espresso, Cappuchino"
print (name + " would you like to order anything from our menu? \n" + menu)

order = input()

price = 5

quantity = input("How many coffees would you like? \n")


total = price * int(quantity)
print ("Thank you, your total is " +  "$" + str(total))

print ("Sounds good " + name + " we'll have your " + quantity + " " + order + " ready for you in a moment")


