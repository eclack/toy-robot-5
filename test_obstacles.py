import world.obstacles
import sys
import unittest
from unittest.mock import patch
from io import StringIO
unittest.util._MAX_LENGTH = 2000

class TestObstacles(unittest.TestCase):
	def test_path_blocked(self):
		world.obstacles.obstacles = [(0,20)]
		self.assertEqual(world.obstacles.is_path_blocked(0,22,0,0),True)
	
	def test_path_blocked_2(self):
		world.obstacles.obstacles = [(10,0)]
		self.assertEqual(world.obstacles.is_path_blocked(12,0,0,0),True)

	



if __name__ == "__main__":
	unittest.main()