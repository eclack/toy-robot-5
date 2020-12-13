from world.text import world as text_world
from world.turtle import world as turtle_world
import unittest
from unittest.mock import patch
import sys
from io import StringIO

class TestWorlds(unittest.TestCase):
	
	def test_get_obstacles_text(self):
		text_world.setup()
		self.assertGreater(len(text_world.obstacles_list), 0)
	
	def test_get_obstacles_turtle(self):
		turtle_world.setup()
		self.assertGreater(len(turtle_world.obstacles_list),0)


if __name__ == "__main__":
	unittest.main()