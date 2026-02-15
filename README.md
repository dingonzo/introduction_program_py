# Introduction-program.py
[![Python Package using Conda](https://github.com/dingonzo/introduction-program/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/dingonzo/introduction-program/actions/workflows/python-package-conda.yml) 

This Python script is an interactive introductory program that demonstrates basic user input, conditional logic, and random number generation. Great for a beginner programmer to reference!

# The Welcome & Setup
Input Collection: It asks for your name and stores it as a string.
User Interface: It prints a personalized welcome message and uses an input() prompt to act as a pause. The script won't move forward until you press the "Enter" key.
# The Comparison Logic
The script performs a basic mathematical comparison between a fixed number and a number you provide:
It sets a variable b to 50.
It asks you to enter a number for a.
Logic Check:
If your number is less than 50, it tells you "B is greater than A!"
If your number is exactly 50, it tells you "both numbers are equal!"
If your number is higher than 50, it tells you "A is greater than B!"
# The Random Guessing Game
This is the "game" portion of the script:
Generation: It uses random.randrange(1, 10) to pick a secret number between 1 and 9.
The Guess: It asks you to guess a number.
Result: It compares your guess to the secret number.
If you match, it prints a success message.
If you miss, it reveals what the secret number was.
