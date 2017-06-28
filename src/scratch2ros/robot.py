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


import rospy

from geometry_msgs.msg import Twist
from kobuki_msgs.msg import MotorPower


class Robot():

    """
    Robot class.
    """

    def __init__(self):
        """
        Init method.
        """

        # variables
        self.__cmd = Twist()

        self.__cmd.linear.x = 0.0
        self.__cmd.linear.y = 0.0
        self.__cmd.linear.z = 0.0
        self.__cmd.angular.x = 0.0
        self.__cmd.angular.y = 0.0
        self.__cmd.angular.z = 0.0

        self.__power_cmd = MotorPower()

        # publishers and subscribers
        self.__velocity_pub = rospy.Publisher('mobile_base/commands/velocity',
                                              Twist,
                                              latch=True,
                                              queue_size=1)
        self.__motor_power_pub = rospy.Publisher('mobile_base/commands/motor_power',
                                                 MotorPower,
                                                 latch=True,
                                                 queue_size=1)

    def enable(self):
        """
        .
        """

        self.__power_cmd.state = MotorPower.ON
        self.__motor_power_pub.publish(self.__power_cmd)

        rospy.sleep(1.0)

    def disable(self):
        """
        .
        """

        self.__power_cmd.state = MotorPower.OFF
        self.__motor_power_pub.publish(self.__power_cmd)

        rospy.sleep(1.0)

    def move(self):
        """
        .
        """

        self.__cmd.linear.x = 1.0
        self.__velocity_pub.publish(self.__cmd)

        rospy.sleep(2.0)

    def stop(self):
        """
        .
        """

        self.__cmd.linear.x = 0.0
        self.__velocity_pub.publish(self.__cmd)

        rospy.sleep(2.0)
