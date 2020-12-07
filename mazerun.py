import robot
import sys
import import_helper
# import time
# start_time = time.time()
if len(sys.argv) > 1 and sys.argv[1].lower() == "turtle" :
    import world.turtle.world as world
else :
    import world.text.world as world


if len(sys.argv) > 2:
    if 'maze' in sys.argv[2]:
        obstacles = import_helper.dynamic_import('maze.' + sys.argv[2])
    else:
        obstacles = import_helper.dynamic_import('maze.obstacles')
else:
    obstacles = import_helper.dynamic_import('maze.obstacles')




stored_forward = set()
stored_left_turns = set()
stored_right_turn = set()
end_x = 0
end_y = 0


def next_out_of_bounds():
    """
    Looking if the next block is on the boundry of our maze/safe area.
    """
    if world.current_direction_index == 0 and world.position_y == 200:
        return True
    elif world.current_direction_index == 1 and world.position_x == 100:
        return True
    elif world.current_direction_index == 2 and world.position_y == -200:
        return True
    elif world.current_direction_index == 3 and world.position_x == -100:
        return True
    else:
        return False


def next_blocked():
    """
    Looking if the next block is blocked by an obstacle.
    """
    if world.current_direction_index == 0:
        return obstacles.is_position_blocked(world.position_x, world.position_y + 1)
    elif world.current_direction_index == 1:
        return obstacles.is_position_blocked(world.position_x + 1, world.position_y)
    elif world.current_direction_index == 2:
        return obstacles.is_position_blocked(world.position_x, world.position_y - 1)
    elif world.current_direction_index == 3:
        return obstacles.is_position_blocked(world.position_x - 1, world.position_y)


def right_blocked():
    """
    Looking if the block to the right is blocked by an obstacle.
    """
    if world.current_direction_index == 0:
        return obstacles.is_position_blocked(world.position_x + 1, world.position_y)
    elif world.current_direction_index == 1:
        return obstacles.is_position_blocked(world.position_x, world.position_y - 1)
    elif world.current_direction_index == 2:
        return obstacles.is_position_blocked(world.position_x - 1, world.position_y)
    elif world.current_direction_index == 3:
        return obstacles.is_position_blocked(world.position_x, world.position_y + 1)


def left_blocked():
    """
    Looking if the block to the left is blocked by an obstacle.
    """
    if world.current_direction_index == 0:
        return obstacles.is_position_blocked(world.position_x - 1, world.position_y)
    elif world.current_direction_index == 1:
        return obstacles.is_position_blocked(world.position_x, world.position_y + 1)
    elif world.current_direction_index == 2:
        return obstacles.is_position_blocked(world.position_x + 1, world.position_y)
    elif world.current_direction_index == 3:
        return obstacles.is_position_blocked(world.position_x, world.position_y - 1)


def end_selector(name, command):
    """
    The end selector funtion looks at the command given ex:(top, bottom, left, right)
    from there we look at what the end point will be.
    after an end point is selected either mazerun_x or _y will run and solve the maze.
    """
    global end_x,end_y
    if command.lower() == 'top' or command.lower() == '':
        end_y = 200
        mazerun_y(name)
    elif command.lower() == 'bottom':
        end_y = -200
        mazerun_y(name)
    elif command.lower() == 'left':
        end_x = -100
        mazerun_x(name)
    elif command.lower() == 'right':
        end_x = 100
        mazerun_x(name)


def mazerun_x(name):
    """
    Solving the maze while pos_x != end_x

    making use of a inverted left hand method(right hand method)
    almost hugging the right wall at all times.
    """
    print(' > '+name+' starting maze run..')
    while not next_blocked() and not next_out_of_bounds():                      #looking if the next block is not blocked and it isnt at the border
        robot.handle_command(name, 'forward 1')
    while world.position_x != end_x:                                            # while current position isnt end position.
        if next_blocked() or next_out_of_bounds():                              # if the next block is blocked or it is out of bounds.
            if (world.position_x,world.position_y) not in stored_left_turns:    # looking if the position is stored in the set or not.
                stored_left_turns.add((world.position_x,world.position_y))      # if it wasn't stored, adding it to the set.
                robot.handle_command(name, 'left')                              
            elif (world.position_x,world.position_y) not in stored_right_turn:  # looking at a set again
                stored_right_turn.add((world.position_x,world.position_y))      # storing if nessecary 
                robot.handle_command(name, 'right')
            else :
                #the U turn of note!
                robot.handle_command(name, 'left')
                robot.handle_command(name, 'left')
                stored_left_turns.discard((world.position_x,world.position_y))  #discarding saved positions so that if robot gets here again it can rerun certain tasks
                stored_right_turn.discard((world.position_x,world.position_y))
        elif not right_blocked():                                               # if the right block is not blocked continue
            if (world.position_x,world.position_y) not in stored_right_turn:    # looking at saved set values again
                stored_right_turn.add((world.position_x,world.position_y))      # storing if nessecary
                robot.handle_command(name, 'right')
            elif (world.position_x,world.position_y) not in stored_forward:     # looking at saved set values again
                stored_forward.add((world.position_x,world.position_y))         # storing if nessecary
                while not next_blocked() and not next_out_of_bounds():
                    robot.handle_command(name, 'forward 1')
            elif (world.position_x,world.position_y) not in stored_left_turns and not right_blocked(): # if current position is nor present in either set: go left(change direction to hopefully not get stuck)
                stored_left_turns.add((world.position_x,world.position_y))
                robot.handle_command(name, 'left')
            else :
                robot.handle_command(name, 'right')
                robot.handle_command(name, 'forward 1')
                stored_forward.discard((world.position_x,world.position_y))
                stored_left_turns.discard((world.position_x,world.position_y))  #discarding saved positions so that if robot gets here again it can rerun certain tasks
                stored_right_turn.discard((world.position_x,world.position_y))  #discarding saved positions so that if robot gets here again it can rerun certain tasks
        else :
            robot.handle_command(name, 'forward 1')
    # print("--- %s seconds ---" % (time.time() - start_time))   


def mazerun_y(name):
    """
    Solving the maze while pos_y != end_y

    making use of a inverted left hand method(right hand method)
    almost hugging the right wall at all times.

    same as above but with different end condition. 
    """
    # can look at above comments as both are almost the same.
    print(' > '+name+' starting maze run..')
    while not next_blocked() and not next_out_of_bounds():
        robot.handle_command(name, 'forward 1')
    while world.position_y != end_y:
        if next_blocked() or next_out_of_bounds():
            if (world.position_x,world.position_y) not in stored_left_turns:
                stored_left_turns.add((world.position_x,world.position_y))
                robot.handle_command(name, 'left')
            elif (world.position_x,world.position_y) not in stored_right_turn:
                stored_right_turn.add((world.position_x,world.position_y))
                robot.handle_command(name, 'right')
            else :
                #the U turn of note!
                robot.handle_command(name, 'left')
                robot.handle_command(name, 'left')
                stored_left_turns.discard((world.position_x,world.position_y))
                stored_right_turn.discard((world.position_x,world.position_y))
        elif not right_blocked():
            if (world.position_x,world.position_y) not in stored_right_turn:
                stored_right_turn.add((world.position_x,world.position_y))
                robot.handle_command(name, 'right')
            elif (world.position_x,world.position_y) not in stored_forward:
                stored_forward.add((world.position_x,world.position_y))
                while not next_blocked() and not next_out_of_bounds():
                    robot.handle_command(name, 'forward 1')
            elif (world.position_x,world.position_y) not in stored_left_turns and not right_blocked():
                stored_left_turns.add((world.position_x,world.position_y))
                robot.handle_command(name, 'left')
            else :
                robot.handle_command(name, 'right')
                robot.handle_command(name, 'forward 1')
                stored_forward.discard((world.position_x,world.position_y))
                stored_left_turns.discard((world.position_x,world.position_y))
                stored_right_turn.discard((world.position_x,world.position_y))
        else :
            robot.handle_command(name, 'forward 1')

    # print("--- %s seconds ---" % (time.time() - start_time))            


def start_mazerunner(name, command):
    """
    This is the main control function for the mazerunner
    resets globals and runs the program
    """
    global stored_forward,stored_left_turns,stored_right_turn,end_x,end_y
    stored_forward.clear()
    stored_left_turns.clear()
    stored_right_turn.clear()
    end_x = 0
    end_y = 0
    end_selector(name, command)
    if command == "top" or command == "bottom" or command == "left" or command == "right":
        return True, ''+name+': I am at the ' +command+ ' edge.'
    else :
        return True, ''+name+': I am at the top edge.'