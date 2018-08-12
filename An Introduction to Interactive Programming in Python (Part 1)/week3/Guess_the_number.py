# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, 100)

    global current_range
    current_range = 1

    global count
    count = int(math.ceil(math.log(100 - 0 + 1, 2)))

    print('New game started')
    print('You have', count, 'guesses')
    print('Please enter your guess number')
    print()


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret_number
    secret_number = random.randrange(0, 100)

    global current_range
    current_range = 1

    global count
    count = int(math.ceil(math.log(100 - 0 + 1, 2)))

    print('New game started')
    print('The range is [0, 100)')
    print('You have', count, 'guesses')
    print('Please enter your guess number')
    print()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret_number
    secret_number = random.randrange(0, 1000)

    global current_range
    current_range = 2

    global count
    count = int(math.ceil(math.log(1000 - 0 + 1, 2)))

    print('New game started')
    print('The range is [0, 1000)')
    print('You have', count, 'guesses')
    print('Please enter your guess number')
    print()


def input_guess(guess):
    # main game logic goes here
    iguess = int(guess)
    print('Guess was', iguess)

    # count the enter times
    global count
    count = count - 1

    # start to compare
    if iguess < secret_number:
        print('Higher')
    elif iguess == secret_number:
        print('Correct')
        print()
        print('New game started!')  # Start a new game

        # to make sure whats the previous range
        if current_range == 1:
            range100()

        elif current_range == 2:
            range1000()

    elif iguess < secret_number:
        print('Lower')

    # show times remaining
    print('Guesses remaining:', count)

    # to see whether lose this game
    if count == 0:
        print('You lose!', 'The correct number is:', secret_number)
        if current_range == 1:
            print()
            range100()

        elif current_range == 2:
            print()
            range1000()
    print()

# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
frame.add_input('Enter guess number!', input_guess, 100)
button1 = frame.add_button('Range is [0,100) ', range100, 130)
button2 = frame.add_button('Range is [0,1000)', range1000, 130)
frame.start()

# call new_game
new_game()

# always remember to check your completed program against the grading rubric
