#What is the price of a child's meal? 4.50
#What is the price of an adult's meal? 9.00
#How many children are there? 4
#How many adults are there? 2
#What is the sales tax rate? 6

#Subtotal: $36.00
#Sales Tax: $2.16
#Total: $38.16

#What is the payment amount? 40
#Change: $1.84

num_appetizers = 0
appetizers_price = 0
kids_meal = 0
num_kids = 0
amount_paid = 0

print()
if input('Do you want any appetizers? (yes/no) ') == 'yes':
    num_appetizers = int(input('How many appetizers do you want? '))
    appetizers_price = float(input('what is the price of a appetizer? '))

if input('Are there any kids? (yes/no) ') == 'yes':
    num_kids = int(input('How many children are there? '))
    kids_meal = float(input('What is the price of a child' + "'" + 's meal? '))

adults_meal = float(input('What is the price of an adult' + "'" + 's meal? '))

num_adult = int(input('How many adults are there? '))

tax = float(input('What is the sales tax rate? '))

appetizer_total = float(num_appetizers * appetizers_price)
kids_total = float(kids_meal * num_kids)
adults_total = float(adults_meal * num_adult)
sub = float(kids_total + adults_total + appetizer_total)

subtotal = sub
sales_tax = sub * tax / 100
total = sub + sales_tax

print()
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')

print()
while amount_paid < total - 0.01:
    amount_paid = float(input('What is the payment amount? '))
    change = amount_paid - total
    total = total - amount_paid
    amount_paid = 0
    if amount_paid < total - 0.01:
        print(f'Not enough, you still own ${total:.2f}')
        print()


print(f'Change: ${change:.2f}')
print('Have a nice day!')
