

def school_age_calculator(age, name):
    if age < 5:
        print ("Enjoy the time!", name, "is only", age)
    elif age == 5:
        print ("Enjoy Kindergarden, " , name)
    else:
        print ("They grow up so fast!")

school_age_calculator(6, "Thomas")