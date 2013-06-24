# template for "Stopwatch: The Game"

import simplegui

# define global variables
counter = 0
x = 0 #stops made at whole seconds
y = 0 #stops attempted 

isStopped = False #checks if the timer is already stopped 

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D

#format(0) == 0:00.0
#format(11) = 0:01.1
#format(321) = 0:32.1
#format(613) = 1:01.3
    
def format(t):
    A = t // 600
    B = (t // 100) % 10
    C = (t // 10) % 10
    D = t % 10
    
    strB = ""
        
    if B == 0 or B >= 6:
        strB = "0"
    else: 
        strB = str(B)
   
    return str(A) + ":" + strB + str(C) + "." + str(D)

# helper function to count every 5 seconds
def isFullSecond():
    return (counter % 10 == 0)

# helper function to update x & y
def update_xy():
    global x, y, isStopped
    if not isStopped:
        x += 1
        if isFullSecond():
            y += 1    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter),[100, 100], 24, "White")
    canvas.draw_text(str(x)+"/"+str(y),[20, 30], 18, "Green")

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global isStopped
    timer.start()
    isStopped = False
    
def stop_handler():
    global isStopped
    timer.stop()
    update_xy()
    isStopped = True
    
def reset_handler():
    global counter, x, y, isStopped
    counter, x, y = 0, 0, 0
    timer.stop()
    isStopped = True
    
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1

# create frame
frame = simplegui.create_frame("Stopwatch",300,200)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)    

frame.set_draw_handler(draw)

frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)

# start timer and frame
#timer.start()
frame.start()
# remember to review the grading rubric