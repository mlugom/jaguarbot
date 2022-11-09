#usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Node():
    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher('cmd_vel_rpi',Twist,queue_size=10)
        self.sub = rospy.Subscriber('cmd_vel',Twist,self.callback)

        rospy.init_node('bridge',anonymous=True)


    def callback(self,data):
        self.cmd_vel_pub.publish(data)
        rospy.loginfo("I've published a new Msg")

if __name__ == '__main__':
    node = Node()
    rospy.spin()