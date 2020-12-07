import unittest
from unittest.main import main
from unittest.mock import patch
from io import StringIO
import world.text.world as world
from maze import obstacles as obs
import robot
import sys

class test_Worlds(unittest.TestCase):


    def test_forward(self):
        sys.stdout = StringIO()
        obs.random.randint = lambda a, b: 0
        self.assertEqual(world.do_forward("Hal", 5), (True, ' > Hal moved forward by 5 steps.'))
        robot.robot_reset()


    def test_back(self):
        sys.stdout = StringIO()
        obs.random.randint = lambda a, b: 0
        self.assertEqual(world.do_back("Hal", 5), (True, ' > Hal moved back by 5 steps.'))
        robot.robot_reset()


    def test_Right(self):
        sys.stdout = StringIO()
        obs.random.randint = lambda a, b: 0
        self.assertEqual(world.do_right_turn("Hal"), (True, ' > Hal turned right.'))
        robot.robot_reset()


    def test_Left(self):
        sys.stdout = StringIO()
        obs.random.randint = lambda a, b: 0
        self.assertEqual(world.do_left_turn("Hal"), (True, ' > Hal turned left.'))
        robot.robot_reset()


    def test_sprint(self):
        sys.stdout = StringIO()
        
        world.do_sprint("hal", 10)
        self.assertEqual(sys.stdout.getvalue(), """ > hal moved forward by 10 steps.
 > hal moved forward by 9 steps.
 > hal moved forward by 8 steps.
 > hal moved forward by 7 steps.
 > hal moved forward by 6 steps.
 > hal moved forward by 5 steps.
 > hal moved forward by 4 steps.
 > hal moved forward by 3 steps.
 > hal moved forward by 2 steps.
""")
        robot.robot_reset()


    @patch("sys.stdin", StringIO("hal\nforward 20\nback 20\noff\n"))
    def test_position(self):
        sys.stdout = StringIO()
        obs.random.randint = lambda a, b: 0
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? hal: Hello kiddo!
hal: Loaded obstacles.
hal: What must I do next?  > hal moved forward by 20 steps.
 > hal now at position (0,20).
hal: What must I do next?  > hal moved back by 20 steps.
 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..
""")
        robot.robot_reset()


if __name__ == "__main__":
    unittest.main()