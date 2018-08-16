# template for "Stopwatch: The Game"

# Import modules
import simplegui

# define global variables
width = 200
height = 200
interval = 100
postion = [60, 100]
time = 0
totalplaytime = 0
wintime = 0
postion1 = [150, 50]
runningtimer = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    # format the time
    t = time
    min = int(t / 600)  # get A
    t = t - min * 600  # get the remainder
    sec1 = int(t / 100)  # get B
    t = t - sec1 * 100  # get the remainder
    sec2 = int(t / 10)  # get C
    t = t - sec2 * 10  # get the remainder
    sec3 = t  # the rest is D
    formatted_time = str(min) + ':' + str(sec1) + str(sec2) + '.' + str(sec3)

    return formatted_time


# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start_handler():
    timer.start()

    global runningtimer
    runningtimer = True


def button_stop_handler():
    timer.stop()

    # to check whether you win the game
    global totalplaytime, wintime, runningtimer  # global these that we can change the value
    if time % 10 == 0 and runningtimer == True:
        totalplaytime = totalplaytime + 1
        wintime = wintime + 1
        runningtimer = False
    elif runningtimer == True:
        totalplaytime = totalplaytime + 1
        runningtimer = False


def button_reset_handler():
    timer.stop()  # stop the timer

    # reset values to zero
    global time, totalplaytime, wintime, runningtimer
    time = 0
    totalplaytime = 0
    wintime = 0
    runningtimer = False


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time + 1
    format(time)


# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), postion, 36, "Red")
    canvas.draw_text(str(wintime) + '/' + str(totalplaytime), postion1, 25, "Green")


# create frame
frame = simplegui.create_frame("Home", width, height)

# crete buttons
button_start = frame.add_button('Start', button_start_handler, 100)
button_stop = frame.add_button('Stop', button_stop_handler, 100)
button_reset = frame.add_button('Reset', button_reset_handler, 100)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
