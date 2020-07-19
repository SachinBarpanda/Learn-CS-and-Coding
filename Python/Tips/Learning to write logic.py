import random 

##Adding an empty variable to 
winner = ''

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

##The below block of while loop code is executed only if user_choice != [rock,
##paper, scissors], which is true for the first try at least as user_choice is
##an empty variable
user_choice = ''
while (user_choice != 'rock' and
       user_choice != 'paper' and
       user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')

if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

if winner == 'Tie':
    print('We both chose', computer_choice + ', play again.')
else:
    print(winner, 'won. The computer chose', computer_choice + '.')