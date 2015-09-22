#!/usr/bin/env python
"""Emergency Stop for Neato: Class Version"""

import rospy
from neato_node.msg import Bump
from geometry_msgs.msg import Twist, Vector3
from tf.transformations import euler_from_quaternion


class EStop(object):
	def __init__(self):
		rospy.init_node('emergency_stop')
		self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
		rospy.Subscriber("/bump", Bump, self.process_bump)
		self.has_bumped = False

	def process_bump(self, msg):
		self.bumpsum = msg.leftFront + msg.leftSide + msg.rightFront + msg.rightSide
		if self.bumpsum > 0:
			self.has_bumped = True
		else:
			self.has_bumped = False

	def run(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			if self.has_bumped:
				self.pub.publish(Twist())
			else:
				self.pub.publish(Twist(linear=Vector3(x=0.1)))
			r.sleep()



if __name__ == '__main__':
	node = EStop()
	node.run()
