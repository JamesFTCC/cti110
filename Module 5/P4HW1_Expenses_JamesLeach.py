# CTI-110
# P4HW1 - Expenses
# James Leach
# 10/10/19

# Inputs the user's amount in account and expenses.
# Calculates the amount left in account after suntracting expenses.
# Outputs the orignal amount, number of expenses, and amount left when expenses are subtracted.

start = 'Y'
num = 1
expenses = 0
initial = float(input('Enter the Starting Amount in Your Account: '))

    
while start == 'Y' or start == 'y':
    expense=float(input('Enter Amount of Expense {}: '. format(num)))
    num += 1
    start = input('Would you like to enter another expense? (Y/N)')
    expenses += expense
    amount = initial - expenses

num = num - 1

print('Amount in Account Before Expenses: ${:,.2f}'.format(initial))
print('Number of Expenses Entered:',num)
print('Amount in Account After Expenses: ${:,.2f}'.format(amount))


