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
        
        @param ic: 
        @param node: 
        """

        # variables
        self.__vel = CMDVel()
        self.__motors_client = comm.getMotorsClient(ic, "robot.Motors", node)
        self.__laser_client = comm.getLaserClient(ic, "robot.Laser", node)
        
    def __publish(self, vel):
        """
        .
        
        @param vel: 
        """
        
        self.__motors_client.sendVelocities(vel)
        time.sleep(1)

    def get_laser_values(self):
        """
        .
        
        @return: the average measure from the frontal laser data.
        """
        
        laser = self.__laser_client.getLaserData()
        
        total_data = len(laser.values)
        num_data = 20
        range1 = total_data / 2 - 10
        range2 = total_data / 2 + 10

        
        return sum(laser.values[range1:range2]) / num_data
        
    def move(self, vel=None):
        """
        .
        
        @param vel: 
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
        
        @param vel: 
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
