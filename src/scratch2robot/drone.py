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

#~ from parallelIce.cameraClient import CameraClient
#~ from parallelIce.navDataClient import NavDataClient
#~ from parallelIce.pose3dClient import Pose3DClient
from parallelIce.cmdvel import CMDVel
from parallelIce.extra import Extra


class Drone():

    """
    Drone class.
    """

    def __init__(self, ic, node):
        """
        Init method.

        @param ic: The ICE controller.
        @param node: The ROS node controller.
        """

        #~ self.record = False
        self.takeoff = False
        self.reset = False
        
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
        
    def reset(self):
        """
        
        """
        
        if self.reset == True:
            self.extra.reset()
            self.reset = False
        else:
            self.extra.reset()
            self.reset = True

    def set_xyz_values(self, new_x, new_y):
        """
        
        @param new_x: 
        @param new_y: 
        """
        
        self.cmdvel.setVX(-new_y)
        self.cmdvel.setVY(-new_x)
        
        self.cmdvel.sendVelocities()

    def set_zyaw_values(self, new_z, new_yaw):
        """
        
        @param new_z: 
        @param new_yaw: 
        """
        
        self.cmdvel.setVZ(-new_z)
        self.cmdvel.setYaw(new_yaw)
        
        self.cmdvel.sendVelocities()

    def stop(self):
        """
        
        """
        
        #~ if self.record == True:
            #~ self.extra.record(False)
            
        self.cmdvel.sendCMDVel(0, 0, 0, 0, 0, 0)
            
    def take_off(self):
        """
        
        """
        
        self.extra.takeoff()
            
    def land(self):
        """
        
        """
        
        self.extra.land()
