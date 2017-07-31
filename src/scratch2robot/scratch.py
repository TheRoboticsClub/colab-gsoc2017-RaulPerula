#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def execute(robot):
    try:
        while True:
            robot.move("forward")
            time.sleep(2)
            robot.stop()
            robot.turn("left")
            time.sleep(3)
    
    except KeyboardInterrupt:
        raise
