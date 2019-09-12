# Using Turtle to draw a specific design
# 9/10/19
# CTI-110 P2HW2 - Turtle Graphic
# James Leach

# Imports turtle which allows the program to draw the design
import turtle

# Increases the size of the pen in which the turtle draws with
turtle.pensize(5)

# Makes the "turtle" hidden so it can not be seen while drawing
turtle.hideturtle()

# Draws the outer edges of the design
turtle.forward(150)
turtle.right(45)
turtle.forward(212.1)
turtle.right(45)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(45)
turtle.forward(212.1)
turtle.right(45)
turtle.forward(150)

# Stops the turtle from drawing while moving to a position and then allows it to draw again once it is at the position
turtle.penup()
turtle.setpos(150,0)
turtle.pendown()

# Draws a vertical straight line down the center of the design
turtle.right(180)
turtle.forward(300)

# Stops the turtle from drawing while moving to a position and then allows it to draw again once it is at the position
turtle.penup()
turtle.setpos(0,-150)
turtle.pendown()

# Draws a horizontal straight line through the center of the design
turtle.left(90)
turtle.forward(300)

# Stops the turtle from drawing while moving to a position and then allows it to draw again once it is at the position
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()

# Draws a diagonal line through the center of the design
turtle.right(45)
turtle.forward(424.2)
