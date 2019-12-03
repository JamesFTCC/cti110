# This program has the user add or subtract random numbers.
# 11/5/19
# CTI-110 P5HW2 - Math Quiz
# James Leach

# Inputs whether the user would like to add, subtract, or exit. Then inputs their answer to the problem.
# Calculates whether the users answer was correct.
# Outputs if the user got the problem right or wrong.

import random

def main():
    print('MAIN MENU')
    print('---------')
    print('1) Add Random Numbers')
    print('2) Subtract Random Numbers')
    print('3) Exit')
    quiz=int(input())
    if quiz == 1:
        add_numbers()

    elif quiz == 2:
        subtract_numbers()

def add_numbers():
    x = random.randint(100, 999)
    y = random.randint(100, 999)
    correct = x + y
    print(' ', x)
    print('+', y)
    answer = int(input())
    if correct == answer:
        print('Good Job! You got it right!')
        print('')
        main()
    else:
        print('Sorry, the correct answer was',correct)
        print('')
        main()

def subtract_numbers():
    x = random.randint(100, 999)
    y = random.randint(100, 999)
    correct = x - y
    print(' ', x)
    print('-', y)
    answer = int(input())
    if correct == answer:
        print('Good Job! You got it right!')
        print('')
        main()
    else:
        print('Sorry, the correct answer was',correct)
        print('')
        main()

main()

