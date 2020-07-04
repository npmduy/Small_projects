from random import randint

print ("Choose: Rock, Paper, Scissors")
userChoice = input()

choices = ["rock", "paper", "scissors"]
computerChoice = choices[randint(0,2)]

print('---')
print('You chose: ', userChoice)
print('Computer chose: ', computerChoice)
print('---')

if userChoice.lower() == computerChoice:
    result = 'Draw!'
elif userChoice.lower() == 'rock' and computerChoice == 'scissors':
    result = 'You won! Rock > Scissors'
elif userChoice.lower() == 'scissors' and computerChoice == 'paper':
    result = 'You won! Scissors > Paper'
elif userChoice.lower() == 'paper' and computerChoice == 'rock':
    result = 'You won! Paper > Rock'
elif userChoice.lower() == 'rock' and computerChoice == 'paper':
    result = 'You lost! Rock < Paper'
elif userChoice.lower() == 'scissors' and computerChoice == 'rock':
    result = 'You lost! Scissors < Rock'
elif userChoice.lower() == 'paper' and computerChoice == 'scissors':
    result = 'You lost! Paper < Scissors'

print (result)