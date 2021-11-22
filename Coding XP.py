
# Lets try Coding

print ("hello world")
#Eivind was a 22 year young boy who worked in the mechanical indusry
#Eivind didnt like his job and wanted to start programming /coding like his brother


character_name = "Eivind"
character_age = "22"
a = "programming"
is_male = True

print ("There once was a man named " + character_name + ",")
print ("This man wanted to become a programmer,")
print ("But he did not know how to start "+ a + "")
print ("So Eivind did what he does best, improvised")
print ("Eivind was " + character_age + " when he tried out programming")

character_name = " Ørjan"
b = "programmer"
is_male = True

print ("There once was a man named " + character_name + ",")
print ("This man became a "+ b +" ,")

print ("Giraffe\nAcademy")
phrase = "Eivind og Ørjan"
print (phrase + " er tvillinger")
print (phrase.upper())
print (phrase.islower())

print (phrase.upper().isupper()) # Makes the phrase uppercase then checks if it is giving true or false

print (len(phrase))
print (phrase[1]) # Printed letter number 2 since youre counting from 0

print (phrase.index("d")) # Found the d in Eivind and numberized its spot

print (phrase.replace("Eivind", "Jimmy"))  # Eivind got replaced with Jimmy in the print


a=1000
intrest=1.1

result = a * intrest ** 5
print (result)

print (3*(4+5))

print (10%3) # % = Modulus, it gives out whats remaining

my_num = -1337
print (my_num)
print (str(my_num)+ " is my favorite number")
 # print ((my_num)+ " is my favorite number") will not work

print (abs(my_num))

print(pow(4,6)) # This will result in 4 being ^6  (4 is powered by 6)
print (max(9,100)) #will print highest number
print (min(9,100)) # vice versa
print (round(8.51))

from math import * 
print (floor(3.7))  #round down
print (ceil(3.7))

print (sqrt(46))

