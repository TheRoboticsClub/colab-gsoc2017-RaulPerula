#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def execute(robot):
    try:
        while True:
            
                robot.move("forward")
            else:
                robot.turn("left")
            
    
    except KeyboardInterrupt:
        raise
