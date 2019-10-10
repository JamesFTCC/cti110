# Displays total number of bugs collected after five days
# 10/8/19
# CTI-110 P4T2 - Bug Collector
# James Leach

# Inputs number of bugs collected for each day.
# Adds bugs collected each day together.
# Outputs total number of bugs collected.

total = 0

for day in range(1, 6):
    print('Enter the number of bugs you collected on day',day)
    bugs = int(input())
    total += bugs

print("You've collected a total of",total,"bugs.")
    
