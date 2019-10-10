# CTI-110
# P4T1B - Initials
# James Leach
# 10/3/19

# Imports 'turtle' and its written instructions.
# Draws lines based on the turtle's input.
# Outputs the letters J and L.

import turtle

james=turtle.Turtle()
james.speed(100)
james.pensize(25)
james.color('purple')

james.right(90)
james.forward(200)

for x in range(180):
    james.forward(.9)
    james.right(1)

james.penup()
james.goto(110,0)
james.pendown()

james.right(180)
james.forward(248)
james.left(90)
james.forward(100)





