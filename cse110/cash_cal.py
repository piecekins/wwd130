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

kids_meal=float(input('What is the price of a child'+"'"+'s meal? '))
adults_meal=float(input('What is the price of an adult'+"'"+'s meal? '))

num_kids=int(input('How many children are there? '))
num_adult=int(input('How many adults are there? '))

tax=float(input('What is the sales tax rate? '))

kids_total=float(kids_meal*num_kids)
adults_total=float(adults_meal*num_adult)
sub=float(kids_total+adults_total)
subtotal=round(sub,2)
print()
print('Subtotal: $'+str(subtotal))