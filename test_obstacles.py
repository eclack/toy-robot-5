import unittest
import robot
from maze import obstacles as obstacles

class Test_Obstacles(unittest.TestCase):

    def test_is_position_blocked_yes(self):
        obstacles.obstacle_list = [(77, 89), (13, -105)] 
        self.assertEqual(obstacles.is_position_blocked(77, 92), True)
        robot.robot_reset()


    def test_is_position_blocked_no(self):
        obstacles.obstacle_list = [(77, 89), (13, -105)]
        self.assertEqual(obstacles.is_position_blocked(18, -110), False)
        robot.robot_reset()


    def test_is_path_blocked_yes(self):
        obstacles.obstacle_list = [(77, 89), (13, -105)]
        self.assertEqual(obstacles.is_path_blocked(70 , 91, 80, 91), True)
        robot.robot_reset()


    def test_is_path_blocked_no(self):
        obstacles.obstacle_list = [(77, 89), (13, -105)]
        self.assertEqual(obstacles.is_path_blocked(15 , 50, 15, -12), False)
        robot.robot_reset()


if __name__ == "__main__":
   unittest.main()