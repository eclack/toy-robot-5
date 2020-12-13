import robot

try:
    if robot.argv[1] == 'turtle':
        from world.turtle import world as text_world
    else:
        from world.text import world as text_world
except IndexError:
    import world.text.world as text_world


# Globals to store turns that have been made
made_right_turns = set()
made_left_turns = set()
open_side_space = set()
been_before = set()


def start_mazerun(robot_name,command_arg):
	"""
	Starts all the initiation for the mazerun
	"""
	global wanted_exit
	if command_arg.lower() == "top" or command_arg == "":
		wanted_exit = "top"
	if command_arg.lower() == "right":
		wanted_exit = "right"
	if command_arg.lower() == "left":
		wanted_exit = "left"
	if command_arg.lower() == "bottom":
		wanted_exit = "bottom"

	print(f" > {robot_name} starting maze run..")
	start_moving(robot_name)
	if escaped:
		return True, (f" > {robot_name} now at the {wanted_exit} edge.")


def add_to_right_turns():
	global made_right_turns
	x = text_world.position_x
	y = text_world.position_y
	made_right_turns.add((x,y))


def check_escaped():
	x = text_world.position_x
	y = text_world.position_y
	direction = text_world.current_direction_index

	if wanted_exit == "top" or wanted_exit == "":
		if direction == 0 and y == 200:
			return True
	if wanted_exit == "right":
		if direction == 1 and x == 100:
			return True
	if wanted_exit == "bottom":
		if direction == 2 and y == -200:
			return True
	if wanted_exit == "left":
		if direction == 3 and x == -100:
			return True
	return False



def left_not_blocked():
	x = text_world.position_x
	y = text_world.position_y
	direction = text_world.current_direction_index

	if direction == 0:
		return text_world.is_position_allowed(x-1,y,x,y)
	if direction == 1:
		return text_world.is_position_allowed(x,y+1,x,y)
	if direction == 2:
		return text_world.is_position_allowed(x+1,y,x,y)
	if direction == 3:
		return text_world.is_position_allowed(x,y-1,x,y)
	return False


def right_not_blocked():
	x = text_world.position_x
	y = text_world.position_y
	direction = text_world.current_direction_index

	if direction == 0:
		return text_world.is_position_allowed(x+1,y,x,y)
	if direction == 1:
		return text_world.is_position_allowed(x,y-1,x,y)
	if direction == 2:
		return text_world.is_position_allowed(x-1,y,x,y)
	if direction == 3:
		return text_world.is_position_allowed(x,y+1,x,y)
	return False	


def is_pos_block():
	x = text_world.position_x
	y = text_world.position_y
	direction = text_world.current_direction_index

	if direction == 0:
		return text_world.is_position_allowed(x,y+1,x,y)
	if direction == 1:
		return text_world.is_position_allowed(x+1,y,x,y)
	if direction == 2:
		return text_world.is_position_allowed(x,y-1,x,y)
	if direction == 3:
		return text_world.is_position_allowed(x-1,y,x,y)
	return False


def check_in_right_turns():
	x = text_world.position_x
	y = text_world.position_y
	if (x,y) in made_right_turns:
		return True
	return False


def check_in_left_turns():
	x = text_world.position_x
	y = text_world.position_y
	if (x,y) in made_left_turns:
		return True
	return False


def remove_pos():
	global made_left_turns,made_right_turns
	x = text_world.position_x
	y = text_world.position_y
	if (x,y) in made_left_turns and made_right_turns:
		made_left_turns.remove((x,y))
		made_right_turns.remove((x,y))


def out_of_bounds():
	x = text_world.position_x
	y = text_world.position_y
	direction = text_world.current_direction_index
	
	if wanted_exit == "top" or "":
		if direction == 1 and x+1 == 100:
			return True
		if direction == 2 and y-1 == -200:
			return True
		if direction == 3 and x-1 == -100:
			return True
	if wanted_exit == "right":
		if direction == 0 and y+1 == 200:
			return True
		if direction == 2 and y-1 == -200:
			return True
		if direction == 3 and x-1 == -100:
			return True
	if wanted_exit == "bottom":
		if direction == 0 and y+1 == 200:
			return True	
		if direction == 1 and x+1 == 100:
			return True
		if direction == 3 and x-1 == -100:
			return True
	if wanted_exit == "left":
		if direction == 0 and y+1 == 200:
			return True
		if direction == 1 and x+1 == 100:
			return True
		if direction == 2 and y-1 == -200:
			return True
	return False


def start_moving(robot_name):
	global escaped
	escaped = False
	while not escaped:
		while is_pos_block() and not out_of_bounds():
			if check_been_before()
			robot.handle_command(robot_name,"forward 1")
			escaped = check_escaped()

		
		if right_not_blocked() and not check_in_right_turns():
			robot.handle_command(robot_name,"right")
			add_to_right_turns()
		elif left_not_blocked() and not check_in_left_turns():
			robot.handle_command(robot_name,"left")
		elif not left_not_blocked() and check_in_right_turns():
			robot.handle_command(robot_name,"right")
		elif check_in_left_turns() and check_in_right_turns():
			robot.handle_command(robot_name,"right")
			robot.handle_command(robot_name,"right")
			remove_pos()