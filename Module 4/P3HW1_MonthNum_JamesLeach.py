# CTI-110
# P3HW1 - Month Number
# James Leach   
# 9/24/19
#

#Gets the number of the month from the user and assigns it to a variable
month=float(input('What is the number of the month? '))

#Determines what month to display based on the value of the variable
if month==1:
    print('January')
elif month==2:
    print('February')
elif month==3:
    print('March')
elif month==4:
    print('April')
elif month==5:
    print('May')
elif month==6:
    print('June')
elif month==7:
    print('July')
elif month==8:
    print('August')
elif month==9:
    print('September')
elif month==10:
    print('October')
elif month==11:
    print('November')
elif month==12:
    print('December')

#If the variable is not any of the values above a message appears
else:
    print('Number not in range.')
