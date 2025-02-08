'''
What is the first number? 4
What is the second number? 3
The first number is greater
The numbers are not equal
The second number is not greater

What is your favorite animal? giraffe
That one is not my favorite.
'''

my_animal = 'eagle' 

first_num = input('What is the first number? ')
second_num = input('What is the second number? ')

if first_num > second_num:
    print('The first number is greater')
else: 
    print('The first number not greater')

if first_num == second_num:
    print('The numbers are equal')
else: 
    print('The numbers are not equal')

if first_num < second_num:
    print('The second number is greater')
else: 
    print('The second number not greater')

print()
animal = input('What is your favorite animal? ')

if animal.lower() == my_animal:
    print('That'+"'"+'s my favorite animal too!') 
else:
    print('That one is not my favorite.')