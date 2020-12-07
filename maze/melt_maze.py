import random

# list of all obstacles
obstacle_list = []


def give_space(tup):
    for i in range(len(obstacle_list)):
        if (tup[0] in range(obstacle_list[i][0] - 7, obstacle_list[i][0] + 6)) and (tup[1] in range(obstacle_list[i][1] - 7, obstacle_list[i][1] + 6)):
            return True
    return False

def get_obstacles():
    """
    Creates a list of tuples representing the coords of all the obstacles
    """
    global obstacle_list
    for i in range(random.randint(300, 350)):
        obstacle_tup = (random.randint(-100, 100), random.randint(-200, 200))
        while give_space(obstacle_tup):
            obstacle_tup = (random.randint(-100, 100), random.randint(-200, 200))
        obstacle_list.append(obstacle_tup)
    return obstacle_list


def is_position_blocked(x,y):
    """
    Returns True is supplied coords are within an obstacle 
    """
    for i in range(len(obstacle_list)):
        if (obstacle_list[i][0] <= x <= (obstacle_list[i][0] + 4)) and (obstacle_list[i][1] <= y <= (obstacle_list[i][1] + 4)):
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Returns True is there is an obstacle between to points of x or y coords
    """
    if x1 == x2:
        for y in range(sorted([y1, y2])[0], sorted([y1, y2])[1] + 1):
            if is_position_blocked(x1, y):
                return True
    else:
        for x in range(sorted([x1, x2])[0], sorted([x1, x2])[1] + 1):
            if is_position_blocked(x, y1):
                return True
    return False

# get_obstacles()
