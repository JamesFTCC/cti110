# This program calculates the total cost of a meal purchased at a restaurant
# 9/3/19
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# James Leach
#

# Gets the user's cost of food, aswell as tip and tax percentages
cost = float(input('Cost of food? '))
tip_percent = float(input('Tip percentage? (Enter as a Decimal) '))
tax_percent = float(input('Tax percentage? (Enter as a Decimal) '))

# Calculates tip by multiplying the user's cost and tip percentage
tip = cost * tip_percent

# Calculates tax by multiplying the user's cost and tax percentage
tax = cost * tax_percent

# Displays tip and tax amount
print('Tip Amount = $', format(tip, ',.2f'))
print('Tax Amount = $', format(tax, ',.2f'))

# Calculates the total cost by adding the cost, tip, and tax
total_cost = cost + tip + tax

# Displays the total cost of the user's meal
print('Total Cost = $', format(total_cost, ',.2f'))
