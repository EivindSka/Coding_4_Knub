from typing import Text


coordinates = (4, 5)
print(coordinates[1])

coordinates = [4, 5]
coordinates[1] = 20
print(coordinates)

# Tuple om verdien ikke skal forandres
# List du kan redigere som du vil

my_var = "dark knight"
print(my_var.title())

with open("lines.txt") as file_data:  # Opened file lines and printed
    data = file_data.read()
print(data)


msg1 = "Ørjan picked up {} blueberries from the {} bushes"
msg1.format(17, 7)

print(msg1)

msg2 = "Ørjan {verb} the {funny} man in the {a}"
msg2.format(verb="shot", funny="crazy", a="head")
print(msg2)
