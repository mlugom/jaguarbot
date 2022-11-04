#!usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO

# Constants
signalA_left = 6
signalB_left = 13
signalA_right = 19
signalB_right = 26

def initPins():
    GPIO.setmode(GPIO.BCM)    
    signals = [signalA_left,signalB_left,signalA_right,signalB_right]
    GPIO.setup(signals,GPIO.OUT)
    GPIO.output(signals,False)

def callback(data):
    omegaLeft,omegaRight = inverseKinematics(data)
    # pinX_left and pinX_right correspond to the boolean value to be assigned to the pins.
    pinA_left,pinB_left = setPins(omegaRight)
    pinA_right,pinB_right = setPins(omegaRight)

    GPIO.output(signalA_left,pinA_left)
    GPIO.output(signalB_left,pinB_left)
    GPIO.output(signalA_right,pinA_right)
    GPIO.output(signalB_right,pinB_right)


def motorCommander():
    rospy.init_node('motorCommander',anonymous=True)

    rospy.Subscriber('cmd_vel',Twist,callback)

    rospy.spin()

def inverseKinematics(data):
    l = 0.3
    r = 0.03
    # Robot velocities
    x_vel = data.linear.x
    theta_vel = data.angular.z

    # Motor velocities
    omegaLeft = int((2*x_vel - l*theta_vel)/(2*r))
    omegaRight = int(-(2*x_vel + l*theta_vel)/(2*r))

    return omegaLeft,omegaRight

def setPins(omega):
    pinA = False
    pinB = False
    if omega > 0:
        pinA = True
    elif omega < 0:
        pinB = True
    
    return pinA,pinB


if __name__ == '__main__':
    initPins()
    motorCommander()