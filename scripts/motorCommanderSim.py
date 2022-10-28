#!usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# Global variables

messageGlob = 'Stop'
def callback(data,message):
    getMessage(data,message)


def listener():
    # Initialize subscriber node    
    rospy.Subscriber('cmd_vel',Twist,callback)    

    #rospy.spin()

def getMessage(data,message):    
    x_vel = data.linear.x
    theta_vel = data.angular.z
    if x_vel > 0:
        message = 'Forward'
    elif x_vel < 0:
        message = 'Backward'
    elif theta_vel > 0:
        message = 'Turn left'
    elif theta_vel < 0:
        message = 'Turn right'
    else:
        message = 'Stop'
        
def motorCommander():
    rospy.init_node('motorCommander', anonymous=True)
    pub = rospy.Publisher('chatter',String, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        listener()
        pub.publish(messageGlob)
        rate.sleep()

class Node:
    def __init__():
        self.pub = rospy.Publisher('chatter',String,queue_size=10)
        self.sub = rospy.Subscriber()


if __name__ == '__main__':
    message = 'Stop'
    try:
        pub = rospy.Publisher('chatter',String,queue_size=10)
        rospy.init_node('motorCommander', anonymous=True)
        rate = rospy.Rate(1)

        while not rospy.is_shutdown():
            rospy.Subscriber('cmd_vel',Twist,callback(message))
            rospy.loginfo(message)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass