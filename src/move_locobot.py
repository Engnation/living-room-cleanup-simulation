#! /usr/bin/env python 

import rospy 
from geometry_msgs.msg import Twist 

class PublishData(): 

    def __init__(self): 

        self.pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=1) 
        self.msg = Twist() 
        self.msg.linear.x = 0.2 
        self.rate = rospy.Rate(1)   

    def publish_msg(self): 

        while not rospy.is_shutdown(): 
            rospy.loginfo("Publisihg Twist message...") 
            self.pub.publish(self.msg) 
            self.rate.sleep() 

if __name__ == '__main__': 

    rospy.init_node("publish_data") 
    publishdata_object = PublishData() 
    publishdata_object.publish_msg() 