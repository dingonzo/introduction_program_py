######################################################################
#Author: Edgar Gonzalez
#Date: August 28, 2022
######################################################################

# import random module to invoke randrange() function for generating
# random numbers within a range.
import random


# Ask user for their name, cast input as 'string' data.
input_name = str(input('Please enter your first name: '))

# print the welcome message including the user's name.
print('\n\nWelcome, ' + input_name + ', to Python Programming!')
# pause screen here to wait for user to press enter to begin.
null = input("Press enter to begin comparison...")


# Ask the user to enter a number and
# compare it to static literal '50'.
# accept user input and cast input as 'numeric' data.
a = int(input("\n\nIf B = 50, Enter a number for A: "))
b = 50
if b > a:
    print("B is greater than A!")
elif b == a:
    print("both numbers are equal!")
else:
    print("A is greater than B!")

# Pause screen here to wait for user to press enter to begin.
null = input("Press enter to begin guessing game..")

# Guess a number game.
random_num = random.randrange(1,10)
guess = int(input("\n\nGuess a number between 1 and 10: "))
if guess == random_num:
    print("Correct, you guessed: {} and the random number generated was: {}".format(str(guess), str(random_num)) )
else:
    print(f"The random number returned was: {str(random_num)} and you guessed: {str(guess)}")

# Pause screen here to wait for user to press enter to begin.
null = input("Press Enter to terminate the program...")




