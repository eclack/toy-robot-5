import random

obstacles = []

def create_obstacles():
    global obstacles
    #bottom wall
    for i in range(-60,100):
        obstacles.append((i,-200))
    #right wall
    for i in range(-200,160):
        obstacles.append((100,i))
    #top wall
    for i in range(-100,-20):
        obstacles.append((i,200))
    for i in range(20,100):
        obstacles.append((i,200))
    #left wall
    for i in range(-200,0):
        obstacles.append((-100,i))
    for i in range(40,200):
        obstacles.append((-100,i))
    #for bottom wall spike
    for i in range(-200,-160):
        obstacles.append((20,i))
    #for wall curl
    for i in range(-100,-20):
        obstacles.append((i,-80))
    for i in range(-160,-40):
        obstacles.append((-20,i))
    for i in range(-60,-20):
        obstacles.append((i,-160))
    for i in range(-160,-120):
        obstacles.append((-60,i))
    for i in range(-20,20):
        obstacles.append((i,-120))
    for i in range(-20,20):
        obstacles.append((i,-40))
    for i in range(-80,-40):
        obstacles.append((20,i))
    for i in range(20,60):
        obstacles.append((i,-80))
    for i in range(-160,-80):
        obstacles.append((60,i))
    #right wall spike
    for i in range(60,100):
        obstacles.append((i,-40))
    #left wall spike
    for i in range(-100,-60):
        obstacles.append((i,40))
    #top spike
    for i in range(120,200):
        obstacles.append((60,i))
    #top left curl spike
    for i in range(160,200):
        obstacles.append((-20,i))
    for i in range(-20,20):
        obstacles.append((i,160))
    #middle obstacles
    for i in range(60,100):
        obstacles.append((i,40))
    for i in range(0,40):
        obstacles.append((60,i))
    for i in range(80,120):
        obstacles.append((60,i))
    for i in range(20,60):
        obstacles.append((i,120))
    for i in range(40,120):
        obstacles.append((20,i))
    for i in range(20,60):
        obstacles.append((i,0))
    for i in range(-20,20):
        obstacles.append((i,40))
    for i in range(-60,-20):
        obstacles.append((i,0))
    for i in range(-40,40):
        obstacles.append((-60,i))
    for i in range(-60,20):
        obstacles.append((i,120))
    for i in range(80,160):
        obstacles.append((-60,i))
    for i in range(-60,-20):
        obstacles.append((i,80))


def is_position_blocked(x, y):
    """Loops through object_list to see if the
       parameter coordinates is inside one of the objects

    Args:
        x_cor (int): x coordinate to be checked if in any object
        y_cor (int): y coordinate to be checked if in any object

    Returns:
        Boolean : True if coordinates is in an object else false
    """
    for obs in obstacles:
        if (obs[0] <= x <= obs[0] + 4 and
           obs[1] <= y <= obs[1] + 4):
           return True
    return False


def is_path_blocked(x1, x2, y1, y2):
    """loops through coordinates between x1, y1 and x2, y2
       and calls is_position_blocked to see if there is an object
       in the path

    Args:
        x1 (int): starting x
        y1 (int): starting y
        x2 (int): ending x
        y2 (int): ending y

    Returns:
        Boolean: True if there is an object on the path else false
    """
    direction_x = 1 if x2 >= x1 else -1
    direction_y = 1 if y2 >= y1 else -1
    for x in range(x1, x2 + direction_x, direction_x):
        for y in range(y1, y2 + direction_y, direction_y):
            if is_position_blocked(x, y):
                return True
    return False


def get_obstacles():
    """
    Returns the list of obstacles to draw with
    """
    create_obstacles()
    return obstacles
