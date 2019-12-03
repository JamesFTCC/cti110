# This program converts feet to inches
# 10/29/19
# CTI-110 P5T2_FeetToInches
# James Leach

# Inputs the number of feet from the user.
# Converts the feet to inches by multiplying.
# Outputs the number of inches

convert = 12

def main():
    feet = float(input('Enter the number of feet: '))

    print(feet,'is equal to',feet_to_inches(feet), 'inches.')
def feet_to_inches(feet):

    return feet * convert

main()
