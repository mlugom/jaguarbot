#!usr/bin/env python

import rospy
from std_msgs import String

def callback(data):
    rospy.loginfo(data)

def triggerer():
    rospy.init_node('Triggerer',anonymous=True)
    rospy.Subscriber('take_photo',String,callback)
    rospy.spin()

if __name__ == '__main__':
    triggerer()