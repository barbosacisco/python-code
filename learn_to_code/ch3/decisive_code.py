# This is a Rock, Paper, Scissors game.

import random

options = ['rock', 'paper', 'scissors']

comp_choice = random.choice(options)

print('##### Welcome to Rock, Paper Scissors game! #####\n')

user_choice = input('Please choose: \n 1. Rock \n 2. Paper \n 3. Scissors \n \n')

# Assign value block below.

if user_choice == '1':
    user_choice = 'rock'

elif user_choice == '2':
    user_choice = 'paper'

elif user_choice == '3':
    user_choice = 'scissors'

# Decision block below.

if comp_choice == user_choice:
    print('We have a Tie. No winner this time.')

elif comp_choice == 'rock' and user_choice == 'paper':
    print('Computer has chosen', comp_choice,', you won! Congratulations!.')

elif comp_choice == 'paper' and user_choice == 'scissors':
    print('Computer has chosen', comp_choice,', you won! Congratulations!.')

elif comp_choice == 'scissors' and user_choice == 'rock':
    print('Computer has chosen', comp_choice,', you won! Congratulations!.')

else:
    print('You have chosen', user_choice,'and Computer has chosen', comp_choice,', sorry, you lost.')

"""
TODO:

- Add invalid option check;
- Add loop to ask if the user wants to continue playing after the match is over. 

"""