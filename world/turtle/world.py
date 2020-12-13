import turtle
import math
import random
import import_helper as ih
from maze import obstacles

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

obstacles_list = []

#Reason for not being able to move
reason = ''


def draw_obstacles(turtleboi):
    turtleboi._tracer(False)
    # print("There are some obstacles:")
    turtleboi.pencolor("red")
    for i in obstacles_list:
        x = i[0]
        y = i[1]
        # print(f"- At position {x},{y} (to {x+4},{y+4})")
        turtleboi.penup()
        turtleboi.goto(x,y)
        turtleboi.pendown()
        turtleboi.begin_fill()
        turtleboi.goto(x+4,y)
        turtleboi.goto(x+4,y+4)
        turtleboi.goto(x,y+4)
        turtleboi.goto(x,y)
        turtleboi.end_fill()
    turtleboi._tracer(True)
        



def setup(robot_name,argv):
    """
    Sets up the main screen for turtle
    """
    global turtleboi
    turtleboi = turtle.Turtle()

    #Setting up border
    turtleboi.penup()
    turtleboi.speed(1000)
    turtleboi.goto(100,200)
    turtleboi.pencolor("cyan")
    turtleboi.pensize(3)
    turtleboi.pendown()
    turtleboi.goto(-100,200)
    turtleboi.goto(-100,-200)
    turtleboi.goto(100,-200)
    turtleboi.goto(100,200)
    turtleboi.penup()

    #Setting up the obstacles
    global obstacles_list,module
    try:
        module = ih.dynamic_import(f"maze.{argv[2]}")
        print(f"{robot_name}: Loaded {argv[2]}")
    except IndexError:
        module = ih.dynamic_import("maze.obstacles")
    obstacles_list = module.get_obstacles()
    draw_obstacles(turtleboi)
    turtleboi.penup()
    turtleboi.goto(0,0)
    turtleboi.left(90)
    turtleboi.speed(2)
    turtleboi.pencolor("black")
    turtleboi.pensize(0.5)
    turtleboi.pendown()

def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y, old_x, old_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    global reason
    if module.is_path_blocked(new_x, new_y,position_x, position_y):
        reason = True
        return False
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    current_x,current_y = turtleboi.pos()
    current_x = math.floor(current_x)
    current_y = math.floor(current_y)
    # print(f"Current X: {current_x}, Current Y: {current_y}")
    if directions[current_direction_index] == 'forward':
        new_y = current_y + steps
        new_x = current_x
    elif directions[current_direction_index] == 'right':
        new_x = current_x + steps
        new_y = current_y
    elif directions[current_direction_index] == 'back':
        new_y = current_y - steps
        new_x = current_x
    elif directions[current_direction_index] == 'left':
        new_x = current_x - steps
        new_y = current_y

    if is_position_allowed(new_x, new_y, current_x, current_y):
        global position_x,position_y
        position_x,position_y = new_x,new_y
        return True
    
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        turtleboi.forward(steps)
        x,y = turtleboi.pos()
        math.floor(x)
        math.floor(y)
        turtleboi.goto(x,y)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    if reason:
        return True, f' > {robot_name}: Sorry there is an obstacle in the way.'
    else:
        return True, f'{robot_name}: Sorry, I cannot go outside my safe zone'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        turtleboi.back(steps)
        x,y = turtleboi.pos()
        math.floor(x)
        math.floor(y)
        turtleboi.goto(x,y)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    if reason:
        return True, f' > {robot_name}: Sorry there is an obstacle in the way.'
    else:
        return True, f'{robot_name}: Sorry, I cannot go outside my safe zone'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    turtleboi.right(90)
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    turtleboi.left(90)
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)