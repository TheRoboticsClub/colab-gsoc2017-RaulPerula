#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__copyright__ = "JdeRobot project"
__credits__ = ["Raul Perula-Martinez"]
__license__ = "GPL v3"
__version__ = "0.0.0"
__maintainer__ = "Raul Perula-Martinez"
__email__ = "raules@gmail.com"
__status__ = "Development"

import roslib
import rospkg
import rospy
import scratch

from geometry_msgs.msg import Twist
from kobuki_msgs.msg import MotorPower
from robot import Robot

pkg_name = 'scratch2ros'
roslib.load_manifest(pkg_name)


class Executor():

    """
    Executor class.
    """

    def __init__(self):
        """
        Init method.
        """

        self.__robot = Robot()

    def run(self):
        """
        Main loop.
        """

        # enable motors
        self.__robot.enable()

        # execute scratch program
        scratch.execute(self.__robot)

        # disable motors
        self.__robot.disable()


if __name__ == '__main__':
    try:
        # start the node
        rospy.init_node(pkg_name)

        # create the node
        node = Executor()

        # spin the node
        node.run()
    except rospy.ROSInterruptException:
        pass
