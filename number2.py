
# module import
import random
import sys
attempts = 0
# user_guess = raw_input("Guess my number!:")
chosen_number = random.randrange(1,101)
# print chosen_number

print "Welcome"

# allows user to repeatedely guess number, also tells user how close they are to number
def game(chosen_number, attempts):
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
                answer = raw_input("Restart? y/n:") 
                if answer == "n":
                    print "Leaving the game"
                    sys.exit(0) # import sys module 
                elif answer == "y":
                    print "Starting new game"
                    game(chosen_number, attempts)
                
        if attempts == 10:
            print "oops you have run out of turns"
            
        # restart = raw_input("would you like to play agian? ")
        # if restart == yes:
        # attempts = 0
        # game(chosen_number, attempts)
game(chosen_number, attempts)        
        
answer = raw_input("Restart? y/n:") 
if answer == "n":
    print "Leaving the game"
    sys.exit(0) # import sys module 
elif answer == "y":
    print "Starting new game"
    game(chosen_number, attempts)

   



