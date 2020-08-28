#! /usr/bin/env python 

import rospy 
from geometry_msgs.msg import Twist 

class PublishData(): 

    def __init__(self,steps): 

        self.pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=1) 
        self.msg = Twist() 
        self.msg.linear.x = 0.2 
        self.rate = rospy.Rate(1)
        self.steps_count = steps 

    def publish_msg(self): 

        while not rospy.is_shutdown(): 
            rospy.loginfo("Publisihg Twist message...") 
            self.pub.publish(self.msg) 
            self.rate.sleep() 

    def publish_msg_count(self): 
        i = 0

        while i < self.steps_count: 
            rospy.loginfo("Publisihg Twist message...") 
            self.pub.publish(self.msg) 
            self.rate.sleep() 
            i += 1

    def stop_robot(self): 
        self.msg.linear.x = 0 
        self.msg.linear.y = 0 
        self.publish_msg()
if __name__ == '__main__': 

    rospy.init_node("publish_data") 
    publishdata_object = PublishData(4) 
    publishdata_object.publish_msg_count()
    publishdata_object.stop_robot() 