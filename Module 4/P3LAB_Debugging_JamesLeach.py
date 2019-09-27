# CTI-110
# P3LAB - Debugging
# James Leach
# 9/24/19
#

# Inputs user's score
# Determines what grade the user got based on their score
# Outputs the user's score

score=float(input('What is your score? '))

A_score=90
B_score=80
C_score=70
D_score=60

if score >= A_score:
    print('Your grade is A.')
elif score >= B_score:
    print('Your grade is B.')
elif score >= C_score:
    print('Your grade is C.')
elif score >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')
