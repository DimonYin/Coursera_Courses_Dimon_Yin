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
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]

    # randomization to the velocity
    if direction == LEFT:
        ball_vel[0] = -random.randrange(120, 240)
        ball_vel[1] = -random.randrange(60, 180)
    elif direction == RIGHT:
        ball_vel[0] = random.randrange(120, 240)
        ball_vel[1] = -random.randrange(60, 180)


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.randrange(0, 2))
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_pos = [[0, HEIGHT - 100], [0, HEIGHT]]
    paddle2_pos = [[WIDTH, HEIGHT - 100], [WIDTH, HEIGHT]]


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0] / 60
    ball_pos[1] = ball_pos[1] + ball_vel[1] / 60

    # collide and reflect off of left hand side
    if ball_pos[0] <= BALL_RADIUS:
        score2 = score2 + 1  # count wins
        spawn_ball(RIGHT)  # new round

    # collide and reflect off of right hand side
    if ball_pos[0] >= WIDTH - BALL_RADIUS:
        score1 = score1 + 1  # count wins
        spawn_ball(LEFT)  # new round

    # collide and reflect off of bottom
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # collide and reflect off of top
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0][1] = paddle1_pos[0][1] - paddle1_vel
    paddle1_pos[1][1] = paddle1_pos[1][1] - paddle1_vel
    paddle2_pos[0][1] = paddle2_pos[0][1] - paddle2_vel
    paddle2_pos[1][1] = paddle2_pos[1][1] - paddle2_vel

    if paddle1_pos[0][1] < 0:
        paddle1_vel = 0
    if paddle1_pos[1][1] > HEIGHT:
        paddle1_vel = 0
    if paddle2_pos[0][1] < 0:
        paddle2_vel = 0
    if paddle2_pos[1][1] > HEIGHT:
        paddle2_vel = 0

        # draw paddles
    canvas.draw_line([paddle1_pos[0][0], paddle1_pos[0][1]], [paddle1_pos[1][0], paddle1_pos[1][1]], 15, "White")
    canvas.draw_line([paddle2_pos[0][0], paddle2_pos[0][1]], [paddle2_pos[1][0], paddle2_pos[1][1]], 15, "White")

    # determine whether paddle and ball collide
    if ball_pos[0] <= BALL_RADIUS + 15:
        if paddle1_pos[0][1] <= ball_pos[1] <= paddle1_pos[1][1]:
            ball_vel[0] = - ball_vel[0] * 1.1
    if ball_pos[0] >= WIDTH - BALL_RADIUS - 15:
        if paddle2_pos[0][1] <= ball_pos[1] <= paddle2_pos[1][1]:
            ball_vel[0] = - ball_vel[0] * 1.1

            # draw scores
    canvas.draw_text(str(score1), [100, 100], 30, "Red")
    canvas.draw_text(str(score2), [500, 100], 30, "Red")


def keydown(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["w"]:
        if paddle1_pos[0][1] > 0:
            paddle1_vel = 4
    elif key == simplegui.KEY_MAP["s"]:
        if paddle1_pos[1][1] < HEIGHT:
            paddle1_vel = -4
    elif key == simplegui.KEY_MAP["up"]:
        if paddle2_pos[0][1] > 0:
            paddle2_vel = 4
    elif key == simplegui.KEY_MAP["down"]:
        if paddle2_pos[1][1] < HEIGHT:
            paddle2_vel = -4


def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


def button_handler():
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button2 = frame.add_button('Restart', button_handler, 100)

# start frame
new_game()
frame.start()
