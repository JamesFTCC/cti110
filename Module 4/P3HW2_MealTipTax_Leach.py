# CTI-110
# P3HW2 - MealTipTax
# James Leach   
# 9/19/19
#

# Inputs cost of meal and desired tip percentage from user
# Calculates the tip, tax, and total cost of the user's meal
# Outputs tip, tax, and total cost

food_cost=float(input('What was the cost of your meal? '))
tip_percent=input('Would you like to leave a 16%, 18%, or 20% tip? (Enter as a percentage) ')

sales_tax=.06

if tip_percent=='16%':
    tip=food_cost*.16
    tax=food_cost*sales_tax
    print('Food Cost: $',
        format(food_cost, ',.2f'))
    print('Tax: $',
        format(tax, ',.2f'))
    print('Tip: $',
        format(tip, ',.2f'))
    total=food_cost+tip+tax
    print('Total Cost: $',
          format(total, ',.2f'))
    
elif tip_percent=='18%':
    tip=food_cost*.18
    tax=food_cost*sales_tax
    print('Food Cost: $',
        format(food_cost, ',.2f'))
    print('Tax: $',
        format(tax, ',.2f'))
    print('Tip: $',
        format(tip, ',.2f'))
    total=food_cost+tip+tax
    print('Total Cost: $',
          format(total, ',.2f'))
    
elif tip_percent=='20%':
    tip=food_cost*.2
    tax=food_cost*sales_tax
    print('Food Cost: $',
        format(food_cost, ',.2f'))
    print('Tax: $',
        format(tax, ',.2f'))
    print('Tip: $',
        format(tip, ',.2f'))
    total=food_cost+tip+tax
    print('Total Cost: $',
          format(total, ',.2f'))
    
else:
    print('Tip percent invalid.')
    
