#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def execute(robot):
    try:
        while True:
            if ((robot.get_laser_distance()) < 1.5):
                robot.turn("left")
            else:
                robot.move("forward")
            
        
    except KeyboardInterrupt:
        raise
