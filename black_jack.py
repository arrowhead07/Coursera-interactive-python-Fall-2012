# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message = ""
score = 0

#Text positions
DEALER_TXT_POS = [100, 120]
OUTCOME_TXT_POS = [330, DEALER_TXT_POS[1]]
PLAYER_TXT_POS = [DEALER_TXT_POS[0], 350]
MSG_TXT_POS = [OUTCOME_TXT_POS[0],PLAYER_TXT_POS[1]]

#Card positions
DEALER_CARD_POS = [100, 180]
PLAYER_CARD_POS = [DEALER_CARD_POS[0], 410]


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        strCards = []
        for c in self.cards:
            strCards.append(str(c))
        return str(strCards)
        
    def add_card(self, card):
        self.cards.append(card)
        
    def hit(self, deck):
        self.add_card(deck.deal_card())

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        hand_value = 0
        have_ace = False
        for c in self.cards:
            rank = c.get_rank()
            hand_value += VALUES[rank]
            if rank == 'A':
                have_ace = True
        if not have_ace:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
        
    def busted(self):
        return self.get_value() > 21
    
    def draw(self, canvas, p):
        i = 0
        for c in self.cards:
            c.draw(canvas, [p[0] + i*100, p[1]])
            i+=1
            if i >=5:
                break
            
        
# define deck class
class Deck:
    def __init__(self):
        self.cards =[Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()
        
    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)
    
    def __str__(self):
        strCards = []
        for c in self.cards:
            strCards.append(str(c))
        return str(strCards)
        

#define event handlers for buttons


def deal():
    global outcome, message, in_play, my_deck, my_hand, dealer_hand, score

    # your code goes here
    if in_play:
        outcome = "You lose"
        score -=1   
    
    #clear everything
    #if my_deck empty??
    #in_play = False
    message = "Hit or stand?"
    #outcome = ""
    #score = 0
    
    #create deck
    my_deck = Deck()
    
    #create player & dealer hands
    my_hand = Hand()
    dealer_hand = Hand()
    
    #hits both the player and the dealer twice.
    my_hand.hit(my_deck)
    my_hand.hit(my_deck)
    
    dealer_hand.hit(my_deck)
    dealer_hand.hit(my_deck)
    
    #The hands should be printed to the console with an 
    #appropriate message indicating which hand is which.
     
    in_play = True

def hit():
    global my_hand, my_deck, in_play, outcome, score, message
    is_busted = False
    # if the hand is in play, hit the player
    if in_play:
        if my_hand.get_value() <= 21:
            my_hand.hit(my_deck)
            if my_hand.get_value() > 21:
                is_busted = True

    # if busted, assign an message to outcome, update in_play and score
    if is_busted:
        outcome = "You have busted"
        message = "New game?"
        in_play = False
        score -= 1
        
def stand():
    global dealer_hand, my_hand, my_deck, in_play, score, outcome, message
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.hit(my_deck)    
        # assign a message to outcome, update in_play and score
        if dealer_hand.busted():
            outcome = "Dealer has busted"
            score += 1
        elif my_hand.get_value() > dealer_hand.get_value():
            outcome = "You win"
            score += 1
        else:
            outcome = "You lose"
            score -= 1
        message = "New deal?"
        in_play = False
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Backjack", [DEALER_TXT_POS[0]-10, 70], 30, "White")
    canvas.draw_text("Score: " + str(score), [OUTCOME_TXT_POS[0], 70], 25, "Yellow")
    canvas.draw_text("Dealer", DEALER_TXT_POS, 20, "Black")
    dealer_hand.draw(canvas,DEALER_CARD_POS)
    canvas.draw_text("Player", PLAYER_TXT_POS, 20, "Black")	
    my_hand.draw(canvas,PLAYER_CARD_POS)
    canvas.draw_text(outcome, OUTCOME_TXT_POS, 20, "Black")
    canvas.draw_text(message, MSG_TXT_POS, 20, "Black")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [DEALER_CARD_POS[0] +CARD_BACK_SIZE[0]/2,DEALER_CARD_POS[1] +CARD_BACK_SIZE[1]/2], CARD_BACK_SIZE)
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
deal()

# get things rolling
frame.start()


# remember to review the gradic rubric