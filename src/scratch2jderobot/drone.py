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


import math
import time

# TODO
#~ from parallelIce.cameraClient import CameraClient
#~ from parallelIce.navDataClient import NavDataClient
#~ from parallelIce.pose3dClient import Pose3DClient

from parallelIce.cmdvel import CMDVel
from parallelIce.extra import Extra


class Drone():

    """
    Drone class.
    """

    def __init__(self, ic, node=None):
        """
        Init method.

        @param ic: The ICE controller.
        @param node: The ROS node controller.
        """
        
        # TODO
        #~ self.camera = CameraClient(ic, "UAVViewer.Camera", True)
        #~ self.navdata = NavDataClient(ic, "UAVViewer.Navdata", True)
        #~ self.pose = Pose3DClient(ic, "UAVViewer.Pose3D", True)
        
        self.cmdvel = CMDVel(ic, "drone.CMDVel")
        self.extra = Extra(ic, "drone.Extra")

    def close(self):
        #~ self.camera.stop()
        #~ self.navdata.stop()
        #~ self.pose.stop()
            pass

    def go_up_down(self, direction):
        """
        Set the straight movement of the drone.

        @param direction: direction of the move. Options: forward (default), back.
        """
        
        # set default velocity (m/s)
        vz = 0.0
        
        if direction == "down":
            vz = -vz
        
        # assign velocity
        self.cmdvel.setVZ(vz)
        
        # publish movement
        self.cmdvel.sendVelocities()

    def move(self, direction):
        """
        Set the straight movement of the drone.

        @param direction: direction of the move. Options: forward (default), back.
        """
        
        # set default velocities (m/s)
        vx = 5.0
        vy = 0.0
            
        # set different direction
        if direction == "back":
            vx = -vx
        elif direction == "left":
            vy = float(vx)
            vx = 0.0
        elif direction == "right":
            vy = float(-vx)
            vx = 0.0
        
        # assign velocities
        self.cmdvel.setVX(vx)
        self.cmdvel.setVY(vy)
        
        # publish movement
        self.cmdvel.sendVelocities()
        
    def turn(self, direction):
        """
        Set the angular velocty.

        @param direction: direction of the move. Options: left (default), right.
        """
        
        # set default velocity (m/s)
        yaw = 5.0 * math.pi
        
        if direction == "right":
            yaw = -yaw
        
        # assign velocity
        self.cmdvel.setYaw(yaw)
        
        # publish movement
        self.cmdvel.sendVelocities()

    def stop(self):
        """
        Set all velocities to zero.
        """
        
        self.cmdvel.setVX(0)
        self.cmdvel.setVY(0)
        self.cmdvel.setVZ(0)
        self.cmdvel.setYaw(0)
        
        self.cmdvel.sendVelocities()
            
    def take_off(self):
        """
        Send the take off command.
        """
        
        self.extra.takeoff()
        time.sleep(1)
            
    def land(self):
        """
        Send the land command.
        """
        
        self.extra.land()
        time.sleep(1)
