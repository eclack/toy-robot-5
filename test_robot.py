import unittest
import robot
from unittest.mock import patch
from io import StringIO
import sys
unittest.util._MAX_LENGTH = 2000

class TestRobot(unittest.TestCase):
	@patch("sys.stdin", StringIO("\nHal\n"))
	def test_robot_name(self):
		sys.stdout = StringIO()

		self.assertEqual(robot.get_robot_name(),"Hal")
		self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? What do you want to name your robot? """)

	@patch("sys.stdin", StringIO("FORWARD 10"))
	def test_get_command(self):
		sys.stdout = StringIO()
		self.assertEqual(robot.get_command("Hal"),"forward 10")

	def test_command_split(self):
		self.assertEqual(robot.split_command_input("forward 10"), ('forward','10'))

	def test_valid_commands_fail(self):
		self.assertEqual(robot.valid_command("jump up"), False)
	
	def test_valid_commands_fail_no_number(self):
		self.assertEqual(robot.valid_command("forward"),False)

	def test_valid_command_pass(self):
		self.assertEqual(robot.valid_command("forward 10"),True)

if __name__ == "__main__":
	unittest.main()
