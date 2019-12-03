# This program converts kilometers to miles
# 10/29/19
# CTI-110 P5T1_KilometerConverter
# James Leach

# Inputs a distance in kilometers.
# Converts the distance to miles by multiplying.
# Outputs the same distance in miles.

convert = 0.6214

def main():
    kilometer = float(input('What is the distance in kilometers? '))

    mile(kilometer)

def mile(km):
    mi = km * convert

    print(km, 'kilometers is equal to', mi, 'miles.')

main()
