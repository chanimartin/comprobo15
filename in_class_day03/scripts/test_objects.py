#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3

rospy.init_node('test_objects')

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

l_1 = Vector3(0.1,0.0,0.0)
a_1 = Vector3(0.0,0.0,0.0)

twist_message = Twist(l_1,a_1)

r = rospy.Rate(1)
i = 0
while not rospy.is_shutdown():
	if i % 2 == 0:
		l_1.x = 0.3
	else:
		l_1.x = -0.3
	pub.publish(twist_message_1)
	r.sleep()
	i += 1