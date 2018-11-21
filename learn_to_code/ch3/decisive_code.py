
# This is a rock, paper, scissors game.

import random

shoushin = ['rock', 'paper', 'scissors']

#print(random.choice(shoushin))

comp_choice = random.choice(shoushin)

print (comp_choice)

user_choice = input('Please make a choice: rock, paper or scissors? ')

if comp_choice == user_choice:
    print('This is a tie!')

elif comp_choice == 'rock' and user_choice == 'paper':
        print('User wins.')

elif comp_choice == 'paper' and user_choice == 'scissors':
    print('User Wins.')

elif user_choice == 'scissors' and comp_choice == 'rock':
    print('Computer Wins.')

elif user_choice == 'rock' and comp_choice == 'paper':
        print('Computer Wins.')

elif user_choice == 'paper' and comp_choice == 'scissors':
    print('Computer Wins.')

elif user_choice == 'scissors' and comp_choice == 'rock':
    print('Computer Wins.')