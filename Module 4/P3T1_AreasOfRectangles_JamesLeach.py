# This code determines if two areas of rectangles are greater than less than or equal to eachother
# 9/17/19
# CTI-110 P3T1 - Areas of Rectangles
# James Leach

#Gets the length and width of the first rectangle from the user and assigns the values to their respective variables
r1l=float(input('What is the length of Rectangle 1? '))
r1w=float(input('What is the width of Rectangle 1? '))

#Gets the length and width of the second rectangle from the user and assigns the values to their respective variables
r2l=float(input('What is the length of Rectangle 2? '))
r2w=float(input('What is the width of Rectangle 2? '))

#Multiplies the length and width of each rectangle to determine both areas
r1area= r1l * r1w
r2area= r2l * r2w

#Compares the two areas and prints a message based on whether they are greater than, less than, or equal to eachother     
if r1area > r2area:
    print('The area of Rectangle 1 is larger.')
if r1area < r2area:
    print('The area of Rectangle 2 is larger.')
if r1area == r2area:
    print('The area of Rectangle 1 is equal to the area of Rectangle 2.')
