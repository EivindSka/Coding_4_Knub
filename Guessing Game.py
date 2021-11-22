
import time
import webbrowser

secret_word = "Tesla"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False


while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit: 
        guess = input ("Enter guess: ")
        guess_count += 1 
        if guess_count == 4:
            print ("This is your last try")
        if guess_count == 2:
            print("Hint: \n It's a stock")       
    else:
        out_of_guesses = True
if out_of_guesses:
    print ("You Lose!")
else:
    print ("You Win, Buy the stonk!")
    time.sleep(5)
    webbrowser.open("https://www.codecademy.com/courses/learn-python/lessons/python-syntax/exercises/print-statements")

#  !=  /  -=  / +=  
