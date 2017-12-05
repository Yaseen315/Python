
# module import
import random

attempts = 0

chosen_number = random.randrange(1,101)
# print chosen_number

print "Welcome"
# allows user to repeatedely guess number, also tells user how close they are to number
while attempts < 10:
    user_guess = raw_input("Guess my number!:")
    if len(user_guess) < 1:
        print "Please put a number"
    elif str.isdigit(user_guess) == False:
        print "Only numbers please!"
    elif int(user_guess) < chosen_number:
        print "Too low"
        attempts += 1
    elif int(user_guess) > chosen_number:
        print "Too high"
        attempts += 1
    elif int(user_guess) == chosen_number:
        print "YES!!!! YOU WON!"
        break 
if attempts == 10:
    print "oops you have run out of turns"
   



