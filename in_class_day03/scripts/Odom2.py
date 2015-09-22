#!/usr/bin/env python
"Autonomously rotate Neato 90 degrees to the right"

import rospy

from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class Odom1(object):
	def __init__(self,target_angle):
		rospy.init_node('Odom2')
		self.theta_goal = target_angle
		self.pub = rospy.Publisher("/cmd_vel",Twist, queue_size = 10)
		rospy.Subscriber ("/odom", Odometry, self.conv_odom)
		self.velocity = 0.0

	def conv_odom(self,msg):
		self.orientation_tuple = (msg.pose.pose.orientation.x, 
								  msg.pose.pose.orientation.y,
								  msg.pose.pose.orientation.z,
								  msg.pose.pose.orientation.w)
		self.angles = euler_from_quaternion(self.orientation_tuple)
		self.theta = self.angles[2]
		self.velocity = 1.0*(self.theta_goal-self.theta)
		print "theta"
		print self.theta
		print "velocity"
		print self.velocity


	def run(self):
		r = rospy.Rate(5)
		while not rospy.is_shutdown():
			self.pub.publish(Twist(angular = Vector3(z = self.velocity)))
			r.sleep()


if __name__=='__main__':
	node = Odom1(1.57)  #angle in radians
	node.run()