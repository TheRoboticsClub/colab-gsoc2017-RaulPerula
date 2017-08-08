#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def execute(robot):
    try:
        while True:
            laser_data = (robot.get_laser_distance())
            if ((laser_data) > 5):
                robot.move("forward")
            else:
                robot.turn("left")
            
    
    except KeyboardInterrupt:
        raise
