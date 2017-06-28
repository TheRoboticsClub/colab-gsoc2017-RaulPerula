#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import robot

def execute():
	for i in range(3):
		robot.stop()
		robot.move()
		rospy.sleep(int("5 secs".replace(" secs", "")))
		robot.stop()
	
	