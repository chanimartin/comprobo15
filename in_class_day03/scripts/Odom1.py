#!/usr/bin/env python
"Autonomously move Neato forward 1m"

import rospy

from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry

class Odom1(object):
	def __init__(self,target_distance):
		rospy.init_node('Odom1')
		self.xgoal = target_distance
		self.pub = rospy.Publisher("/cmd_vel",Twist, queue_size = 10)
		self.velocity = 0.0
		self.sub1 = rospy.Subscriber ("/odom", Odometry, self.process_odom)
		print self.sub1


	def process_odom(self,msg):
		self.xactual = msg.pose.pose.position.x
		self.velocity = 0.5*(self.xgoal - self.xactual)
		print "actual"
		print self.xactual
		print "velocity"
		print self.velocity

	def run(self):
		r = rospy.Rate(5)
		while not rospy.is_shutdown():
			self.pub.publish(Twist(linear = Vector3(x = self.velocity)))
			r.sleep()

if __name__=='__main__':
	node = Odom1(1)  #distance in meters
	node.run()