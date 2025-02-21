
import random

#To have more then one word
secret_number = random.randint(1,10)

#Everything is set to false or nothing
secret_word = ''
win = False
guess = ''
times_guess = 0

#for testing puposes
print(secret_number)

#possible words
if secret_number == 1:
    secret_word = 'lehi'
elif secret_number == 2:
    secret_word = 'alma'
elif secret_number == 3:
    secret_word = 'mormon'
elif secret_number == 4:
    secret_word = 'abinadi'
elif secret_number == 5:
    secret_word = 'nephi'
elif secret_number == 6:
    secret_word = 'ether'
elif secret_number == 7:
    secret_word = 'moroni'
elif secret_number == 8:
    secret_word = 'teancum'
elif secret_number == 9:
    secret_word = 'jacob'
else:
    secret_word = 'zenos'



print('Welcome to the word guessing game!')
print()

while not win:
    guess = input('What is your guess? ')
    times_guess = times_guess + 1

    if guess.lower() != secret_word:
        print('Your guess was not correct.')
    
    if guess.lower() == secret_word:
        win = True
    



print('Congratulations! You guessed it!')
print(f'It took you {times_guess} guesses.')

