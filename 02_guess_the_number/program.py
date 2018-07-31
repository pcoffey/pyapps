import random

print('-----------------------')
print('      NUMBER WANG')
print('-----------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('Player, what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {0} your guess was too low'.format(name, guess))
    elif guess > the_number:
        print('Sorry {0} your guess was too high'.format(name, guess))
    else:
        print('Congrats {0}!! Your guess {1} is correct!!'.format(name, guess))

print('Done')