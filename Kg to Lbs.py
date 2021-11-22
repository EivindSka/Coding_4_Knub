


weight = int(input("Weight: "))
unit = input ("(K)g og (L)lbs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print ("Weigh in lbs: " + str(converted))
else:
    converted = weight * 0.45
    print ("Weigh in kgs: " + str(converted))