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
#import scratch

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
        
        # variables
        self.__cmd = Twist()
        
        self.__cmd.linear.x = 0.0
        self.__cmd.linear.y = 0.0
        self.__cmd.linear.z = 0.0
        self.__cmd.angular.x = 0.0
        self.__cmd.angular.y = 0.0
        self.__cmd.angular.z = 0.0

        sef.__power_cmd = MotorPower()

        # publishers and subscribers
        self.__velocity_pub = rospy.Publisher('mobile_base/commands/cmd_vel',
                                            Twist,
                                            latch=True,
                                            queue_size=1)
        self.__motor_power_pub = rospy.Publisher('mobile_base/commands/motor_power',
                                                MotorPower,
                                                latch=True,
                                                queue_size=1)

    def run(self):
        """
        Main loop.
        """
        
        # enable motors
        self.__power_cmd.state = MotorPower.ON
        self.__motor_power_pub.publish(self.__power_cmd)

        # execute scratch program
        #Scratch.execute()

        for i in range(3):
            # stop
            self.__cmd.linear.x = 0.0
            self.__velocity_pub.publish(self.__cmd)

            # move
            self.__cmd.linear.x = 0.1
            self.__velocity_pub.publish(self.__cmd)

            # sleep
            rospy.sleep(5.0)

            # stop
            self.__cmd.linear.x = 0.0
            self.__velocity_pub.publish(self.__cmd)

            # sleep
            rospy.sleep(2.0)
            
        # disable motors
        self.__power_cmd.state = MotorPower.OFF
        self.__motor_power_pub.publish(self.__power_cmd)


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
