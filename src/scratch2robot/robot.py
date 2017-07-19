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


import jderobotComm as comm
import time

from jderobotTypes import CMDVel


class Robot():

    """
    Robot class.
    """

    def __init__(self, ic, node):
        """
        Init method.
        """

        # variables
        self.__vel = CMDVel()
        self.__client = comm.getMotorsClient(ic, "robot.Motors", node)
        
    def __publish(self, vel):
        """
        .
        """
        
        self.__client.sendVelocities(vel)
        time.sleep(1)

    def move(self, vel=None):
        """
        .
        """
        
        if vel == None:
            # set default velocity (m/s)
            self.__vel.vx = 1.0
        else:
            self.__vel.vx = vel
        
        # publish movement to the robot
        self.__publish(self.__vel)

    def turn(self, vel=None):
        """
        .
        """
        
        if vel == None:
            # set default velocity (m/s)
            self.__vel.az = 1.0
        else:
            self.__vel.az = vel
        
        # publish movement to the robot
        self.__publish(self.__vel)

    def stop(self):
        """
        .
        """
        
        # set default velocities (m/s)
        self.__vel.vx = 0.0
        self.__vel.vy = 0.0
        self.__vel.vz = 0.0
        self.__vel.ax = 0.0
        self.__vel.ay = 0.0
        self.__vel.az = 0.0

        # publish movement to the robot
        self.__publish(self.__vel)
