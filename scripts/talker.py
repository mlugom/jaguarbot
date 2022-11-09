#!usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('talker',anonymous=True)
    pub = rospy.Publisher('chatter',String,queue_size=10)

    rate = rospy.Rate(1) #hz

    while not rospy.is_shutdown():
        msg = 'Hello'
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

