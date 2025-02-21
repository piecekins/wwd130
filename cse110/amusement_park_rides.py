'''
What is the age of the first rider? 12
What is the height of the first rider? 46
Is there a second rider (yes/no)? no
'''

first_rider_age = float(input('What is the age of the first rider? '))
if 17 >= first_rider_age >= 12:
    gold_1 = input('Do you have a golden ticket? ')
first_rider_height = float(input('What is the height of the first rider? '))
second_rider_yes = input('Is there a second rider (yes/no)? ')

if second_rider_yes.lower() == 'yes':
    second_rider_age = float(input('What is the age of the second rider? '))
    if 17 >= second_rider_age >= 12:
        gold_2 = input('Do you have a golden ticket? ')
    second_rider_height = float(input('What is the height of the second rider? '))

if gold_1.lower() == 'yes':
    first_rider_age = 18

if gold_2.lower() == 'yes':
    second_rider_age = 18

elif first_rider_age >= 18 and first_rider_height >= 62:
    may_ride = True

elif (first_rider_age >= 16 and second_rider_age >= 14) or (first_rider_age >= 14 and second_rider_age >= 16):
    may_ride = True

elif first_rider_age >= 12 and second_rider_age >= 12 and first_rider_height >= 52 and second_rider_height >= 52:
    may_ride = True

elif first_rider_height < 36 or second_rider_height < 36 or (first_rider_age < 18 and second_rider_age < 18):
    may_ride = False



else:
    may_ride = True

if may_ride:
    print('You may ride')
else:
    print('you may not ride')
