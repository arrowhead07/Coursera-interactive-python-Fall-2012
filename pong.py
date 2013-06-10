# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2


# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0, 0]
    horz_vel = random.randrange(120, 240) / 60
    vert_vel = random.randrange(60, 180) / 60
    
    if right:
        ball_dir = 1
    else:
        ball_dir = -1
    ball_vel[0] += ball_dir * horz_vel

        
    ball_vel[1] -= vert_vel
    
# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    
    paddle1_pos = paddle2_pos = HEIGHT/2
    paddle1_vel = paddle2_vel = 0
    
    score1 = score2 = 0
    
    #randomly selecting a side for ball spawn
    right = random.randrange(0,2)
    ball_init(right)
    
    
# update paddle's vertical position, keep paddle on the screen
def updatePaddlePos():
    global paddle1_pos, paddle2_pos
    if (paddle1_vel > 0 and (paddle1_pos + paddle1_vel) <= HEIGHT - HALF_PAD_HEIGHT) \
    or (paddle1_vel < 0 and (paddle1_pos + paddle1_vel) >= HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    
    if (paddle2_vel > 0 and (paddle2_pos + paddle2_vel) <= HEIGHT - HALF_PAD_HEIGHT) \
    or (paddle2_vel < 0 and (paddle2_pos + paddle2_vel) >= HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel

def checkBallCollision():
    global score1, score2
    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) or ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        ball_vel[0] *= -1
        
        #right wall, paddle check
        if (ball_pos[0] > WIDTH/2): 
            if (ball_pos[1] < paddle2_pos - HALF_PAD_HEIGHT or ball_pos[1] > paddle2_pos + HALF_PAD_HEIGHT ):
                score1 += 1 
                ball_init(False) #ball to left
            else: ball_vel[0] += .1 * ball_vel[0]
            
        #left wall, paddle check
        if (ball_pos[0] < WIDTH/2):
            if (ball_pos[1] < paddle1_pos - HALF_PAD_HEIGHT or ball_pos[1] > paddle1_pos + HALF_PAD_HEIGHT ):
                score2 += 1
                ball_init(True) #ball to right
            else: ball_vel[0] += .1 * ball_vel[0]
        
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
    # update paddle's vertical position, keep paddle on the screen
    updatePaddlePos()
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    # paddle 1 (left)
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # paddle 2 (right)
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # update ball
    # check for collisions
    checkBallCollision()
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    c.draw_text(str(score1), (WIDTH/4, HEIGHT/5), 30, "White")
    c.draw_text(str(score2), (WIDTH - WIDTH/4 - 10, HEIGHT/5), 30, "White")
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 3
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = (-1) * acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = acc  
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = (-1) * acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel, paddle2_vel = 0, 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()

