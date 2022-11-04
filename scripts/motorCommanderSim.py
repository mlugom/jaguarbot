#!usr/bin/env python

import rospy
from std_msgs.msg import String, Float64
from geometry_msgs.msg import Twist
       


class Node:
    def __init__(self):
        self.pub1 = rospy.Publisher('jaguarbot/left_joint_1_controller/command',Float64,queue_size=10)
        self.pub2 = rospy.Publisher('jaguarbot/left_joint_2_controller/command',Float64,queue_size=10)
        self.pub3 = rospy.Publisher('jaguarbot/left_joint_3_controller/command',Float64,queue_size=10)
        self.pub4 = rospy.Publisher('jaguarbot/right_joint_1_controller/command',Float64,queue_size=10)
        self.pub5 = rospy.Publisher('jaguarbot/right_joint_2_controller/command',Float64,queue_size=10)
        self.pub6 = rospy.Publisher('jaguarbot/right_joint_3_controller/command',Float64,queue_size=10)
        self.sub = rospy.Subscriber('cmd_vel',Twist,self.callback)
        self.message = 'Stop'

        # Robot properties
        self.l = 0.3 #m
        self.r = 0.03 #m

    def callback(self,data):
        omegaLeft,omegaRight = self.inverseKinematics(data)
        self.publish(omegaLeft,omegaRight)

    def inverseKinematics(self,data):
        # Robot velocities
        x_vel = data.linear.x
        theta_vel = data.angular.z

        # Motor velocities
        omegaLeft = int((2*x_vel - self.l*theta_vel)/(2*self.r))
        omegaRight = int(-(2*x_vel + self.l*theta_vel)/(2*self.r))

        return omegaLeft,omegaRight

    def publish(self,omegaLeft,omegaRight):
        self.pub1.publish(omegaLeft)
        self.pub2.publish(omegaLeft)
        self.pub3.publish(omegaLeft)
        self.pub4.publish(omegaRight)
        self.pub5.publish(omegaRight)
        self.pub6.publish(omegaRight)



if __name__ == '__main__':
    node = Node()
    rospy.init_node('motorCommander', anonymous=True)
    rospy.spin()