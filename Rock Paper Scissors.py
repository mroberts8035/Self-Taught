import random


player = input('Enter your name: ')
print()
print()

print('The Rules of the Rock, Paper Scissor game are as follows: \n'
      + 'Paper beats Rock \n'
      + 'Rock beats Scissors \n'
      + 'Scissors beat Paper')
print()
print()

games = int(input('Enter a number for how many games you want to play: '))

win = 0
lose = 0
tie = 0


for i in range(games):
    choice = input('Enter: "1" for Rock, \n       "2" for Paper, \n       "3" for Scissors: ')

    if choice == '1':
        play = 'Rock'
    elif choice == '2':
        play = 'Paper'
    elif choice == '3':
        play = 'Scissors'

    print()
    print('You chose ' + play)


    cpu_choice = random.randint(1, 3)

    if cpu_choice == 1:
        cpu_play = 'Rock'
    elif cpu_choice == 2:
        cpu_play = 'Paper'
    elif cpu_choice == 3:
        cpu_play = 'Scissors'

    print()
    print('The computer chose ' + cpu_play)

    choice = int(choice)
    result = ''

    if choice - cpu_choice == 0:
        result = 'Tie'
    elif choice - cpu_choice in [-2, 1]:
        result = 'Win'
    elif choice - cpu_choice in [-1, 2]:
        result = 'Loss'

    if result == 'Tie':
        tie += 1
    elif result == 'Win':
        win += 1
    elif result == 'Loss':
        lose += 1


    print(result)



print()


print('Wins: ' + str(win))
print('Ties: ' + str(tie))
print('Losses: ' + str(lose))
