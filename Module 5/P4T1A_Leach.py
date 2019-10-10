# CTI-110
# P4T1A - Shapes
# James Leach
# 10/3/19

# Imports the 'turtle' function and its written instructions.
# Loops the code while the variable 'square' is less than or equal to 50.
# Outputs 50 squares that each become larger than the square before it.

import turtle
turtle.hideturtle()
turtle.speed(100)

side=10
square=1

while square<=50:
    for x in range(4):
        turtle.left(90)
        turtle.forward(side)
    side=side+5
    square=square+1
    
