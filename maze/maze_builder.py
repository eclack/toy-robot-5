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


def is_path_blocked(new_x, new_y, old_x, old_y):
    """
    Checks if the path ahead in the new x and y values is blocked by an obstacle
    """
    for pos in obstacles:
        checks = [0,0]
        count_x = old_x
        count_y = old_y
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


def get_obstacles():
    """
    Returns the list of obstacles to draw with
    """
    create_obstacles()
    return obstacles
