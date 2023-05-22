import random
from art import logo

print(logo)
print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')
difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')

tryTimes = 0
if difficulty == 'easy':
    tryTimes = 10
elif difficulty == 'hard':
    tryTimes = 5

answer = random.randint(1, 100)
print(f'Pssst, the correct answer is {answer}')

def checkGuess(guess, answer):
    if guess > answer:
        print('Too high.')
    elif guess < answer:
        print('Too low.')
    else:
        print(f'You got it! The answer was {answer}.')
        return False
    return True

while tryTimes > 0:
    print(f'You have {tryTimes} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))
    if checkGuess(guess, answer):
        tryTimes -= 1
    else:
        break

    if tryTimes == 0:
        print('You\'ve run out of guesses, you lose.')
        break
    else:
        print('Guess again.')


