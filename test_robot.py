import unittest
from unittest.mock import patch
from io import StringIO
from maze import obstacles as obstacles
import robot
import sys


class Test_Robot(unittest.TestCase):

   @patch("sys.stdin", StringIO("Hal"))
   def test_name_robot(self):
      sys.stdout = StringIO()
      obstacles.random.randint = lambda a, b: 0
      self.assertEqual(robot.get_robot_name(), "Hal")
      self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? """)
      robot.robot_reset()


   def test_invalid_command_handle(self):
      sys.stdout = StringIO()
      obstacles.random.randint = lambda a, b: 0
      self.assertFalse(robot.handle_command("Hal","FooooorWarD"))
      self.assertFalse(robot.handle_command("Hal","front"))
      self.assertFalse(robot.handle_command("Hal","BACKWARD"))
      self.assertFalse(robot.handle_command("Hal","Jump Up"))
      self.assertFalse(robot.handle_command("Hal","RUnning"))
      robot.robot_reset()


   def test_get_user_help(self):
      sys.stdout = StringIO()
      obstacles.random.randint = lambda a, b: 0
      self.assertEqual(robot.do_help(), (True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""))
      robot.robot_reset()


   def test_validate_user_input(self):
      sys.stdout = StringIO()
      obstacles.random.randint = lambda a, b: 0
      self.assertTrue(robot.valid_command('forward 20'))
      self.assertFalse(robot.valid_command('Jump Up'))
      self.assertTrue(robot.valid_command('left'))
      self.assertFalse(robot.valid_command('straight'))
      robot.robot_reset()
 

   def test_handle_command(self):
      sys.stdout = StringIO()
      obstacles.random.randint = lambda a, b: 0
      self.assertTrue(robot.handle_command("HAL", "forward 20"))
      self.assertTrue(robot.handle_command('HAL', "back 60"))
      self.assertFalse(robot.handle_command( 'HAL', "off"))
      robot.robot_reset()


   @patch("sys.stdin", StringIO("FoRwArd 20\nBaCK 40\nlEft\nriGHt\nsprinT 10"))
   def test_get_command(self):
      sys.stdout = StringIO()
      obstacles.random.randint = lambda a, b: 0
      self.assertEqual(robot.get_command("HAL"), "forward 20")
      self.assertEqual(robot.get_command("HAL"), "back 40")
      self.assertEqual(robot.get_command("HAL"), "left")
      self.assertEqual(robot.get_command("HAL"), "right")
      self.assertEqual(robot.get_command("HAL"), "sprint 10")
      self.assertEqual(sys.stdout.getvalue(),"""HAL: What must I do next? HAL: What must I do next? HAL: What must I do next? HAL: What must I do next? HAL: What must I do next? """)
      robot.robot_reset()


   @patch("sys.stdin", StringIO("hal\nforward 20\nback 20\nreplay\noff\n"))
   def test_replay(self):
      sys.stdout = StringIO()
      robot.robot_start()
      obstacles.random.randint = lambda a, b: 0
      self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? hal: Hello kiddo!
hal: Loaded obstacles.
hal: What must I do next?  > hal moved forward by 20 steps.
 > hal now at position (0,20).
hal: What must I do next?  > hal moved back by 20 steps.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved forward by 20 steps.
 > hal now at position (0,20).
 > hal moved back by 20 steps.
 > hal now at position (0,0).
 > hal replayed 2 commands.
 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..
""")
      robot.robot_reset()


   @patch("sys.stdin", StringIO("hal\nforward 20\nback 20\nreplay silent\noff\n"))
   def test_replay_silent(self):
      sys.stdout = StringIO()
      robot.robot_start()
      obstacles.random.randint = lambda a, b: 0
      self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? hal: Hello kiddo!
hal: Loaded obstacles.
hal: What must I do next?  > hal moved forward by 20 steps.
 > hal now at position (0,20).
hal: What must I do next?  > hal moved back by 20 steps.
 > hal now at position (0,0).
hal: What must I do next?  > hal replayed 2 commands silently.
 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..
""")
      robot.robot_reset()


   @patch("sys.stdin", StringIO("hal\nforward 20\nback 20\nreplay reversed\noff\n"))
   def test_replay_reversed(self):
      sys.stdout = StringIO()
      robot.robot_start()
      obstacles.random.randint = lambda a, b: 0
      self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? hal: Hello kiddo!
hal: Loaded obstacles.
hal: What must I do next?  > hal moved forward by 20 steps.
 > hal now at position (0,20).
hal: What must I do next?  > hal moved back by 20 steps.
 > hal now at position (0,0).
hal: What must I do next?  > hal moved back by 20 steps.
 > hal now at position (0,-20).
 > hal moved forward by 20 steps.
 > hal now at position (0,0).
 > hal replayed 2 commands in reverse.
 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..
""")
      robot.robot_reset()


   @patch("sys.stdin", StringIO("hal\nforward 20\nback 20\nreplay reversed silent\noff\n"))
   def test_replay_reversed_silent(self):
      sys.stdout = StringIO()
      robot.robot_start()
      obstacles.random.randint = lambda a, b: 0
      self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? hal: Hello kiddo!
hal: Loaded obstacles.
hal: What must I do next?  > hal moved forward by 20 steps.
 > hal now at position (0,20).
hal: What must I do next?  > hal moved back by 20 steps.
 > hal now at position (0,0).
hal: What must I do next?  > hal replayed 2 commands in reverse silently.
 > hal now at position (0,0).
hal: What must I do next? hal: Shutting down..
""")
      robot.robot_reset()


if __name__ == "__main__":
   unittest.main()