import random


obstacles = []

def get_obstacles():
    """Retrieves the list of obstacles
    """
    global obstacles
    number_of_obstacles = random.randint(1,10)
    while number_of_obstacles > 0:
        random_x = random.randint(-100,100)
        random_y = random.randint(-200,200)
        obstacles.append((random_x,random_y))
        number_of_obstacles -= 1
    return obstacles


def is_path_blocked(new_x, new_y, old_x, old_y):
    """
    Checks if the path ahead in the new x and y values is blocked by an obstacle
    """
    for pos in obstacles:
        count_x = old_x
        count_y = old_y
        checks = [0,0]
        if count_y < new_y:
            while count_y <= new_y:
                if count_y in range(pos[1], pos[1]+5):
                    checks[1] = 1
                count_y += 1

        elif count_y > new_y:
            while count_y >= new_y:
                if count_y in range(pos[1], pos[1]+5):
                    checks[1] = 1
                count_y -= 1

        if count_x < new_x:
            while count_x <= new_x:
                if count_x in range(pos[0], pos[0]+5):
                    checks[0] = 1
                count_x += 1
        
        elif count_x > new_x:
            while count_x >= new_x:
                if count_x in range(pos[0], pos[0]+5):
                    checks[0] = 1
                count_x -= 1

        
        if is_position_blocked(new_x,new_y):
            checks[0] = checks[1] = 1
        
        if checks[0] == 1 and checks[1] == 1:
            return True
    return False


def is_position_blocked(new_x,new_y):
    """
    Checks if the position that the robot want to occupy is actually an obstacle space
    """
    for pos in obstacles:
        if new_x in range(pos[0],pos[0]+5) and new_y in range(pos[1],pos[1]+5):
            return True
    return False