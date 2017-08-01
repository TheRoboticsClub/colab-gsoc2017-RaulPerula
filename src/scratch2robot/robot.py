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

        # set default velocities (m/s)
        self.__vel.vx = 1.0
        self.__vel.az = 1.0

        # get clients
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
        Get the average value for the values of the frontal laser.

        @return: the average measure of the frontal laser data.
        """

        laser = self.__laser_client.getLaserData()

        total_data = len(laser.values)
        num_data = 20
        range1 = total_data / 2 - 10
        range2 = total_data / 2 + 10

        return sum(laser.values[range1:range2]) / num_data

    def move(self, direction, vel=None):
        """
        Set the rectilinious movement of the robot.

        @param direction: direction of the move. Options: forward (default), back.
        @param vel: a number with the velocity in m/s. Default: 1 m/s.
        """

        # set different velocity
        if vel != None:
            self.__vel.vx = vel

        # set different direction
        if direction == "back":
            self.__vel.vx = -self.__vel.vx

        # publish movement of the robot
        self.__publish(self.__vel)

    def turn(self, direction, vel=None):
        """
        Set the angular movement of the robot.

        @param direction: direction of the move. Options: left (default), right.
        @param vel: a number with the velocity in m/s. Default: 1 m/s.
        """

        # set different velocity
        if vel != None:
            self.__vel.az = vel

        # set different direction
        if direction == "right":
            self.__vel.az = -self.__vel.az

        # publish movement of the robot
        self.__publish(self.__vel)

    def stop(self):
        """
        .
        """

        # reset velocities (m/s)
        self.__vel.vx = 0.0
        self.__vel.vy = 0.0
        self.__vel.vz = 0.0
        self.__vel.ax = 0.0
        self.__vel.ay = 0.0
        self.__vel.az = 0.0

        # publish movement to the robot
        self.__publish(self.__vel)
