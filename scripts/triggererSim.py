#!usr/bin/env python

import rospy
from std_msgs.msg import String
import cv2
import os.path
import os

def imgNameGenerator(path,basename): # The name is made as a mix of basename and a number.
    i = 0
    while os.path.isfile(f'{path}/{basename}_{i}.png'):
        i += 1

    name = f'{basename}_{i}.png'
    return name

def takePhoto():
    cam = cv2.VideoCapture(0)
    res,img = cam.read()
    if res:
        path = os.getenv("HOME")
        basename = 'photo'
        imName = imgNameGenerator(path,basename)
        cv2.imwrite(f'{path}/{imName}',img)

    cam.release()


def callback(data):
    if data.data == 'Snap':
        takePhoto()

def triggerer():
    rospy.init_node('Triggerer',anonymous=True)
    rospy.Subscriber('take_photo',String,callback)
    rospy.spin()

if __name__ == '__main__':
    triggerer()