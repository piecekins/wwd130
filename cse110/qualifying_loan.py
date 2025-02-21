print('For each of these questions, please provide a 1-10 rating:')

loan_size = float(input('How large is the loan? '))
credit_history = float(input('How good is your credit history? '))
income_size = float(input('How high is your income? '))
down_payment_size = float(input('How large is your down payment? '))

if loan_size >= 5:
    if (credit_history >= 7 and income_size >= 7):
        decision = True
    elif (credit_history >= 7 or income_size >= 7) and down_payment_size >= 5:
        decision = True
    else:
        decision = False

if loan_size < 5:
    if credit_history < 4:
        decision = False
    elif income_size >= 7 or down_payment_size >= 7 or ( income_size >= 4 and down_payment_size >= 4):
        decision = True
    else:
        decision = False




if decision:
    print('yes')
else:
    print('no')