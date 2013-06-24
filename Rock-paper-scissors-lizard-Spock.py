# Rock-paper-scissors-lizard-Spock assignment

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # converting number to a name using if/elif/else
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    else:
        return "scissors"
    
    
def name_to_number(name):
    # converting name to number using if/elif/else
    
    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    else:
        return 4

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # compute difference of player_number and comp_number modulo five
    diff = (player_number - comp_number) % 5
    
 
    # use if/elif/else to determine winner
    
    if(diff >= 1 and diff <= 2):
        # player wins
        result = "Player wins!"
    elif(diff >= 3 and diff <= 4):
        # computer wins
        result = "Computer wins!"
    else:
        #tie
        result = "Player and computer tie!"

    # convert comp_number to name using number_to_name
    
    # print results
    print "Player choose",name
    print "Computer choose", number_to_name(comp_number)
    print result
    print
    
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


