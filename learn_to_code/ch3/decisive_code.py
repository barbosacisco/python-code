# This is a Rock, Paper, Scissors game.

import random

options = ['rock', 'paper', 'scissors']

computer_choice = random.choice(options)

print('##### Welcome to Rock, Paper Scissors game! #####\n')


def initialization():
    global player_choice  # The 'global' function makes the variable 'player_choice' accessible globally.

    player_choice = input('Please choose: \n 1. Rock \n 2. Paper \n 3. Scissors \n \n')

    if player_choice == '1':
        player_choice = 'rock'

    elif player_choice == '2':
        player_choice = 'paper'

    elif player_choice == '3':
        player_choice = 'scissors'


# Check for invalid option.

initialization()  # Calling the function initialization above.

while player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors':
    print('Invalid choice!! Start over.\n')
    initialization()

# Decision block / Code logic.

if computer_choice == player_choice:
    print('We have a Tie. No winner this time.')

elif computer_choice == 'rock' and player_choice == 'paper':
    print('Computer has chosen', computer_choice, ', you won! Congratulations!.')

elif computer_choice == 'paper' and player_choice == 'scissors':
    print('Computer has chosen', computer_choice, ', you won! Congratulations!.')

elif computer_choice == 'scissors' and player_choice == 'rock':
    print('Computer has chosen', computer_choice, ', you won! Congratulations!.')

else:
    print('You have chosen', player_choice, 'and Computer has chosen', computer_choice, ', sorry, you lost.')