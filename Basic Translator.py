

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeoiu":    #if letter in "AEOIUaeoiu":
            if letter.isupper():
                translation = translation + "G"
            translation = translation + "g"
        else:
             translation = translation + letter
    return translation

print (translate(input("Enter a phrase: ")))

# will change every "AEOIUaeoiu" to g