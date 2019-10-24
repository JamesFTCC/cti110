# This code displays a pattern using a nested loop
# 10/24/19
# CTI-110 P4HW3 - Nested Loops
# James Leach

# Inputs x's range of 1-6
# Calculates how many spaces to include inbetween the #'s in each row
# Outputs a pattern using #'s

for x in range(6):
    print('#', end='')
    for y in range(x):
        print(' ', end='')
    print('#')

    
