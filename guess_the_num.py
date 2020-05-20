# This is a guess the number game.
import random

print('Hello! What is your name?')
name = input() # user inputs their name

print(f'{name.title()}, I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

for guessesTaken in range(1, 7): # since you only get 6 guesses (1-6), could also simply write range(6) as well
    print('Take a guess.')
    guess = int(input()) # user inputs a number, but input() is always a string, so need to add int() in front

    if guess < secretNumber:
      print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess

if guess == secretNumber:
    print(f'Excellent, {name}! You guessed my number in {str(guessesTaken)} guesses.') # the variable guessesTaken is an int, so you need to add str() to concatenate to rest of string
else:
    print(f'Nope. The number I was thinking of was {str(secretNumber)}')
    