#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def execute(robot):
    try:
        while True:
            robot.move("forward")
            time.sleep(5)
            robot.stop()
            time.sleep(1)
            robot.turn("left")
            time.sleep(2)
    
    except KeyboardInterrupt:
        raise
