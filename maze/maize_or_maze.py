import random

obstacle_list = []

def get_obstacles():
    """
    generates a maze, of tuples with values: of (x, y) positions to signify walls of a maze.
    """
    global obstacle_list
    obstacle_list = []
    walls_x(-100,-10,196)
    walls_x(10,96,196)
    walls_x(20,100,180)
    walls_x(-12,12,180)
    walls_x(-100,-20,180)
    walls_x(68,100,150)
    walls_x(-15,28,150)
    walls_x(-88,-56,150)
    walls_x(-100,92,126)
    walls_x(-68,72,100)
    walls_x(-30,44,60)
    walls_x(-100,-44,60)
    walls_x(-70,70,20)
    walls_x(-70,70,-20)
    walls_x(-30,44,-60)
    walls_x(-100,-44,-60)
    walls_x(-68,72,-100)
    walls_x(-100,92,-126)
    walls_x(68,100,-150)
    walls_x(-15,28,-150)
    walls_x(-88,-56,-150)
    walls_x(20,100,-180)
    walls_x(-12,12,-180)
    walls_x(-100,-20,-180)
    walls_x(-100,-10,-200)
    walls_x(10,96,-200)
    
    walls_y(-70,10,20)
    walls_y(66,10,20)
    walls_y(-70,-20,-10)
    walls_y(66,-20,-10)
    walls_y(-100,-190,162)
    walls_y(96,150,180)
    walls_y(96,-200,-150)
    walls_y(96,-150,130)
    walls_y(-100,180,196)
    walls_y(96,180,200)
    #print(obstacle_list)
    return obstacle_list


def walls_x(x, x1, y):
    """
    Makes walls on the X axis
    """
    global obstacle_list
    while x < x1:
        obstacle_list.append((x,y))
        x+=4


def walls_y(x, y, y1):
    """
    Makes walls on the Y axis
    """
    global obstacle_list
    while y < y1:
        obstacle_list.append((x,y))
        y+=4





def is_position_blocked(position_x, position_y):
    """
    obs_sort is a sorted list of obstacles:
    for each obstacle in the sorted list-->
    for each x in a + 5 range-->
    for each y in a + 5 range-->
    is either x or y == the position_x or y return a bool of true indicating the position is blocked
    """
    # obs_sort = [sorted(obs) for obs in obstacle_list]
    for obs in obstacle_list:
        # print(obs)
        for x in range(obs[0], obs[0]+5):
            # print(x)
            for y in range(obs[1], obs[1]+5):
                # print(y)
                if position_x == x and position_y == y:
                    return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    if x1 == x2 -->
    sort the y co-ords-->
    for locations in ranges of y1 and y2(using + 1 for range)-->
    if is_position_blocked is called for x1 and the y location-->
    return a bool of true

    ^vice-versa for if y1==y2^
    """
    if x1 == x2:
        y_cords= sorted([y1, y2])
        for loc in range(y_cords[0], (y_cords[1] + 1)):
            if is_position_blocked(x1, loc):
                return True
    elif y1 == y2:
        x_cords = sorted([x1, x2])
        for loc in range(x_cords[0], (x_cords[1] + 1)):
            if is_position_blocked(loc, y1):
                return True
    return False