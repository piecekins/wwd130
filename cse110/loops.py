'''
Please type a positive number: -3
Sorry, that is a negative number. Please try again.
'''

number = -1
answer = ""

number = float(input('Please type a positive number: '))

while number < 0:
    print('Sorry, that is a negative number. Please try again.')
    number = float(input('Please type a positive number: '))

number = str(number)

print('Your number is: ' + number)


answer = input('May I have a piece of candy? ')

while answer.lower() != 'yes':
    answer = input('May I have a piece of candy? ')

print('thank you')


