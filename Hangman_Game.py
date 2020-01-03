
#This part of the code defines the beginning variables
# that will be used later on in my code.

import random
words = ["werm", "pickles", "arthritis", "law", "calculus", "forest", "crisp", "joe"]
secret_word = random.choice(words)
dashes = "-" * len(secret_word)
guesses_left = 10

# This function recieves a guess from the user
# and eliminates any guess that is invalid according
# to the set criteria.

def get_guess():
    while True:
        user_input = input("Guess: ")
        if len(user_input) > 1 or len(user_input) < 1:
            print "Enter only one character!"
        elif not user_input.islower():
            print "Your character must be lowercase!"
        else:
            return str(user_input)

# This function takes three arguments (as given in the
# instructions on CodeHS), and updates the individual
# index where the user guesses correctly.

def update_dashes(secret_word, dashes, user_input):
    for i in range(len(secret_word)):
        if user_input == secret_word[i]:
            dashes = dashes[:i] + user_input + dashes[i+1:]
    return dashes

""" This while loop runs until the user runs out of
guesses or the variable "dashes" does not contain a
value equal to that of the variable "secret_word".
The code then prints dashes which will be updated by
the previous function, update_dashes(), after
the amount of guesses left is printed. """

while guesses_left > 0 and dashes != secret_word:
    print dashes
    print str(guesses_left) + " guesses remaining!"

# newguess is the variable that stores the function
# get_guess(), so it isn't unneccesarilly called.

    newguess = get_guess()

# the variable dashes is redefined by the update_dashes()
# function so when the while loop repeats, it is
# printed redefined with the user's newest guess.

    dashes = update_dashes(secret_word, dashes, newguess)

# This part of the while loop prints whether the
# user's guess was in the secret word or not, and if
# not, subtracts a guess from the variable guesses_left

    if newguess in secret_word:
        print "Your guess is in the word!"
    else:
        print "Sorry, your guess is not in the word."
        guesses_left = guesses_left - 1

# Thise if - else statement ends the game after the
# guesses either run out, or the user guesses the word
# before the amount of guesses runs out.

if guesses_left == 0:
    print "You lose! The word was: " + str(secret_word)
else:
    print "You win! The word was: " + str(secret_word)
