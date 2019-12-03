# This program plays a game in which you have to guess a number
# 10/31/19
# CTI-110 P5HW1 - Random Number
# James Leach

# Inputs the user's decision to play the game and the user's guesses.
# Determines whether the user's guess was right, too low, or too high.
# Outputs whether the user's guess was correct and how many guesses it took, or if the guess was too high or too low.

import random

guess = 0

def main():
    print('MAIN MENU')
    print('---------')
    print('1) Play Game')
    print('2) Exit')
    game=int(input())
    if game == 1:
        random_number()

def random_number():
    x = random.randint(1,100) 
    print('Try to guess a number between 1 and 100!')
    play_game(x)

def play_game(x):
    num = int(input())
    global guess
    guess += 1
    if num == x:
        print('Congratulations! You guessed correctly!')
        print('It only took you',guess,'guesses!')
        print('')
        guess = 0
        main()
    elif num >= x:
        print('Too high, try again.')
        play_game(x)
    elif num <= x:
        print('Too low, try again.')
        play_game(x)

    

main()
