# implementation of card game - Memory

import simplegui
import random

deckOfCards = []
exposed = []
state = 0
card1, card2 = -1, -1 # indices of the exposed cards
counter = 0

# helper function to initialize globals
def init():
    global deckOfCards, exposed, card1, card2, counter, state
    deckOfCards = [i % 8 for i in range(16)]
    exposed = [False for i in range(16)]
    random.shuffle(deckOfCards)
    card1 = card2 = -1
    counter = 0
    state = 0
    l.set_text("Moves = " + str(counter))
            
# define event handlers
def mouseclick(pos):
    global exposed, counter
    for i in range(16):
        if pos[0] > 50 * i and pos[0]< 50 * i + 50: 
            if exposed[i]: break 
            exposed[i] = True
            counter +=1
            l.set_text("Moves = " + str(counter))
            updateState(i)

def updateState(cardIndx):
    global state, card1, card2
     
    if state == 0:
        state = 1
        card1 = cardIndx
    elif state == 1:
        state = 2
        card2 = cardIndx
    elif state == 2:
        if deckOfCards[card1] != deckOfCards[card2]: 
            exposed[card1], exposed[card2] = False, False
        card1, card2 = cardIndx, -1
        state = 1
    
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 0
    for n in deckOfCards:
        if exposed[i]:
            canvas.draw_polygon([(50 * i, 0), (50 * i + 50, 0), (50 * i + 50, 100), (50 * i, 100)], 5, "Black", "Black")
            canvas.draw_text(str(n), [50 * i + 15, 65], 35, "White")
        else:
            canvas.draw_polygon([(50 * i, 0), (50 * i + 50, 0), (50 * i + 50, 100), (50 * i, 100)], 1, "Green", "Green")
            if i > 0:
                canvas.draw_line([50 * i, 0], [50 * i, 100], 3, "Black")
        i += 1
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric