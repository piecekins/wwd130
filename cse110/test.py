
total = 10
amount_paid =0





print()
while amount_paid < total:
    amount_paid = float(input('What is the payment amount? '))
    change = amount_paid - total
    if amount_paid < total:
        print('Not enough please use more money')
        print()
print(change)

