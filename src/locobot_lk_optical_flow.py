#!/usr/bin/env python

#ROS node for LoCoBot using Shi-Tomasi corner point detector and Lucas-Kanade optical flow to track points
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class PointTracker(object):

    def __init__(self):
    
        self.image_sub = rospy.Subscriber("/camera/color/image_raw",Image,self.camera_callback)
        print("image subscription received")
        self.bridge_object = CvBridge()

        # params for ShiTomasi corner detection
        self.feature_params = dict( maxCorners = 100,
                            qualityLevel = 0.3,
                            minDistance = 7,
                            blockSize = 7 )

        # Parameters for lucas kanade optical flow
        self.lk_params = dict( winSize  = (15,15),
                        maxLevel = 2,
                        criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

        # Create some random colors
        self.color = np.random.randint(0,255,(100,3))

    def camera_callback(self,data):
        try:
            # We select bgr8 because its the OpenCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
            print("CV bridge bridging")
        except CvBridgeError as e:
            print(e)

        # Take first frame and find corners in it
        old_gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **self.feature_params)

        # Create a mask image for drawing purposes
        mask = np.zeros_like(cv_image)

        frame_gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

        # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **self.lk_params)

        # Select good points
        good_new = p1[st==1]
        good_old = p0[st==1]

        # draw the tracks
        for i,(new,old) in enumerate(zip(good_new,good_old)):
            a,b = new.ravel()
            c,d = old.ravel()
            mask = cv2.line(mask, (a,b),(c,d), self.color[i].tolist(), 2)
            frame = cv2.circle(cv_image,(a,b),5,self.color[i].tolist(),-1)
        img = cv2.add(cv_image,mask)

        #show_image(cv_image)
        self.show_image(img)

        # Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)

    # Function to show the image in an OpenCV Window    
    def show_image(self,img):
        cv2.imshow("Image Window", img)
        cv2.waitKey(1)

def main():
    rospy.init_node('point_following_node', anonymous=True)
    print("pont following node initiated")

    point_follower_object = PointTracker()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
    main()