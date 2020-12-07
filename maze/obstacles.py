import random

obstacle_list = []

def get_obstacles():
    """
    generates a random list from 1 to 10, of tuples with values: of random (x, y) positions.
    """
    global obstacle_list
    obstacle_list = [(random.randint(-100,100), random.randint(-200,200)) for item in range(random.randint(1,10))]
    return obstacle_list


def is_position_blocked(position_x, position_y):
    """
    obs_sort is a sorted list of obstacles:
    for each obstacle in the sorted list-->
    for each x in a + 5 range-->
    for each y in a + 5 range-->
    is either x or y == the position_x or y return a bool of true indicating the position is blocked
    """
    obs_sort = [sorted(obs) for obs in obstacle_list]
    for obs in obs_sort:
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