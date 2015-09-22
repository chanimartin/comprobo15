#!/usr/bin/env python
"""Emergency Stop for Neato"""

import rospy
from neato_node.msg import Bump
from geometry_msgs.msg import Twist, Vector3


rospy.init_node('emergency_stop')
has_bumped = False
bumpsum = 0

def process_bump(msg):
	global bumpsum
	global has_bumped
	print msg
	bumpsum = msg.leftFront + msg.leftSide + msg.rightFront + msg.rightSide
	if bumpsum > 0:
		has_bumped = True
	else:
		has_bumped = False

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
sub = rospy.Subscriber("/bump", Bump, process_bump)


r = rospy.Rate(10)
while not rospy.is_shutdown():
	if has_bumped == True:
		pub.publish(Twist(linear=Vector3(x=0.00)))
	else:
		pub.publish(Twist(linear=Vector3(x=0.05)))
	#print has_bumped
	print bumpsum
	r.sleep()
