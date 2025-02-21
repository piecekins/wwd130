import random 


win = False
guesses = 0

magic_number = random.randint(1, 100)
#magic_number = input('what is the magic number? ')

while not win:
    guess = int(input('What is your guess? '))

    guesses = guesses + 1
    if guess > magic_number:
        print('Lower')
        
    if guess < magic_number:
        print('Higher')
        
    if guess == magic_number:
        print('You guessed it!!!')
        print(f'You guessed {guesses} times')

        replay = input('Do you want to play again? ')
        if replay.lower() == 'no':
            win = True
            guesses = 0
        else:
            guesses = 0
