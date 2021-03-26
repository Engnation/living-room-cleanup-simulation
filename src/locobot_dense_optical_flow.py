#!/usr/bin/env python

#ROS node for LoCoBot to use dense optical flow to visualize motion
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class DenseMotionTracker(object):

    def __init__(self):
    
        self.bridge_object = CvBridge()

        self.initial_image_sub = rospy.wait_for_message("/camera/color/image_raw",Image, timeout=None)
        print("initial image subscription received")

        initial_image = self.initial_image_sub

        try:
            # We select bgr8 because its the OpenCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(initial_image, desired_encoding="bgr8")
            print("CV bridge bridging")
        except CvBridgeError as e:
            print(e)

        self.prvs = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
        self.hsv = np.zeros_like(cv_image)
        self.hsv[...,1] = 255

        self.continuous_image_sub = rospy.Subscriber("/camera/color/image_raw",Image,self.camera_callback)
        print("second and continued image subscription received")

    def camera_callback(self,data):
        try:
            # We select bgr8 because its the OpenCV encoding by default
            cv_image2 = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
            print("CV bridge bridging")
        except CvBridgeError as e:
            print(e)

        next = cv2.cvtColor(cv_image2,cv2.COLOR_BGR2GRAY)

        flow = cv2.calcOpticalFlowFarneback(self.prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
        self.hsv[...,0] = ang*180/np.pi/2
        self.hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
        rgb = cv2.cvtColor(self.hsv,cv2.COLOR_HSV2BGR)

        #show_image(cv_image)
        self.show_image(rgb)

    # Function to show the image in an OpenCV Window    
    def show_image(self,img):
        cv2.imshow("Image Window", img)
        cv2.waitKey(1)

def main():
    rospy.init_node('point_following_node', anonymous=True)
    print("pont following node initiated")

    dense_motion_object = DenseMotionTracker()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
    main()