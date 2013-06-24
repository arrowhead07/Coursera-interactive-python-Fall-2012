# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
num_chosen = 0
guess = 0
remaining_guess = 0

# define helper function to initialize
def init():
    global remaining_guess, num_chosen
    remaining_guess = math.ceil(math.log(num_range,2))
    num_chosen = random.randrange(0,num_range)
    #print "Chosen", num_chosen
    print "New Game. Range is from 0 to",num_range
    print "Number of remaining guess is", remaining_guess
    print

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range 
    num_range = 100
    init()
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range 
    num_range = 1000
    init()
    
def get_input(guess):
    # main game logic goes here	
    num_guessed = int(guess)
    
    print "Guess was", num_guessed
    global remaining_guess
    remaining_guess = remaining_guess - 1
    print "Number of remaining guess is", remaining_guess
    
    if num_guessed == num_chosen:
        print "Correct!"
        print
        init()
        return
    
    elif num_guessed < 0 or num_guessed > num_range:
        print "Out of range!"
    elif num_guessed > num_chosen:
        print "Lower!"
    else:
        print "Higher!"
    
    print
    
    if remaining_guess == 0:
        print "You ran out of guesses. The number was", num_chosen
        print
        init()
        return
    
   
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# create control elements for window
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

init()

# register event handlers for control elements


# start frame
f.start()

# always remember to check your completed program against the grading rubric
