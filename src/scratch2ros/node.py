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

import robot
import roslib
import rospkg
import rospy
import scratch

from geometry_msgs.msg import Twist
from kobuki_msgs.msg import MotorPower

pkg_name = 'scratch_kobuki'
roslib.load_manifest(pkg_name)


class Executor():

    """
    Executor class.
    """

    def __init__(self):
        """
        Init method.
        """

        pass

    def run(self):
        """
        Main loop.
        """

        # enable motors
        robot.enable()

        # execute scratch program
        # scratch.execute()

        for i in range(3):
            # move
            self.__cmd.linear.x = 1.0
            self.__velocity_pub.publish(self.__cmd)

            rospy.sleep(2.0)

        # disable motors
        robot.disable()


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
