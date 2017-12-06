my_dict = ["discussion", "policeman", "mathematics", "exchange", "mysterious", "rattlesnake", "greenhouse", "wheelbarrow", "dragonfly", "elephant"]

from random import randint

word = ""
char_guesses = ""
wrong_turn = 0
asking = True
final_guess = 0

def word_selector(my_dict, wrong_turn, asking):
    word_num = randint(0, len(my_dict) - 1)
    word = my_dict[word_num]
    word = word.upper()
    print "_" * len(word)
    guess_type(word, wrong_turn, asking, final_guess)


def guess_type(word, wrong_turn, asking, final_guess):
    while asking:
        choice = raw_input("Would you like to guess a letter or the whole word? (Type either 'letter' or 'word') ")
        if choice == "letter":
            asking = user_guess(word, char_guesses, wrong_turn)
        elif choice == "word":
            guess_word = raw_input("Guess a word: ")
            guess_word = guess_word.upper()
            if guess_word == word:
                print "Congratulations, you won!"
                print word
                asking = False
            elif guess_word == "":
                print "Guess invalid. Please enter a word"
            else:
                print "Wrong!"
                final_guess += 1
                if final_guess == 5:
                    print "Too many guesses! You lose!"
                    asking = False
        else:
            print "Invalid input. Please enter 'letter' or 'word'."

guess = ""

def user_guess(word, char_guesses, wrong_turn):
    while wrong_turn < 10:
        if wrong_turn == "":
            break
        else:
            guess = raw_input("Guess a letter: ")
            guess = guess.upper()
            if guess == "":
                print "Guess invalid. Please enter a letter."
            elif len(guess) > 1:
                print "Guess invalid. Please enter only one letter."
            elif guess in char_guesses:
                print "You already guessed that! Try again."
            else:
                char_guesses += guess
                wrong_turn = correct_guess(word, char_guesses, guess, wrong_turn, asking)


def correct_guess(word, char_guesses, guess, wrong_turn, asking):
    i_wrong_turn = wrong_turn
    wrong = 0
    for letter in word:
        if letter in char_guesses:
            print letter,
        else:
            print "_",
            wrong += 1
    if guess not in word:
        i_wrong_turn += 1
        print "Wrong"
        print i_wrong_turn
        if i_wrong_turn == 10:
            print "Sorry! You ran out of turns!"
    else:
        print "You got it right"
        if wrong == 0:
            print "Congratulations! You won!"
            return ""
            asking = False
    return i_wrong_turn

print "HANGMAN!\n"
word_selector(my_dict, wrong_turn, asking)