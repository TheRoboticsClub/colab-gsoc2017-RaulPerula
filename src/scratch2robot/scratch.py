#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

def execute(robot):
    try:
        while True:
            robot.move()
            time.sleep(int("2 secs".replace(" secs", "")))
            robot.stop()
            robot.turn()
            time.sleep(int("3 secs".replace(" secs", "")))
            robot.stop()
    
    except KeyboardInterrupt:
        raise
