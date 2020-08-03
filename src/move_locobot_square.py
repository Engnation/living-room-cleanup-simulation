#! /usr/bin/env python 

import rospy 
from geometry_msgs.msg import Twist 
from std_msgs.msg import String 

class SquareHolo(): 

    def __init__(self): 
        self.pub1 = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1) 
        self.pub2 = rospy.Publisher('/another_topic', String, queue_size=1) 
        self.velocities = Twist() 
        self.msg = String() 
        self.rate = rospy.Rate(1) 

    def linear_vel(self, x=0, y=0): 
        self.velocities.linear.x = x 
        self.velocities.linear.y = y 

    def stop_robot(self): 
        self.velocities.linear.x = 0 
        self.velocities.linear.y = 0 

    def move_square(self): 
        for i in range(4): 
            self.msg.data = "Applying linear velocity in the X axis..." 
            self.pub2.publish(self.msg) 
            self.linear_vel(0.5,0) 
            self.pub1.publish(self.velocities) 
            self.rate.sleep() 

        for i in range(4): 
            self.msg.data = "Applying linear velocity in the Y axis..." 
            self.pub2.publish(self.msg) 
            self.linear_vel(0,0.5) 
            self.pub1.publish(self.velocities) 
            self.rate.sleep() 

        for i in range(4): 
            self.msg.data = "Applying negative linear velocity in the X axis..." 
            self.pub2.publish(self.msg) 
            self.linear_vel(-0.5,0) 
            self.pub1.publish(self.velocities) 
            self.rate.sleep() 

        for i in range(4): 
            self.msg.data = "Applying negative linear velocity in the Y axis..." 
            self.pub2.publish(self.msg) 
            self.linear_vel(0,-0.5) 
            self.pub1.publish(self.velocities) 
            self.rate.sleep() 

        for i in range(4): 
            self.msg.data = "Stopping robot..." 
            self.pub2.publish(self.msg) 
            self.stop_robot() 
            self.pub1.publish(self.velocities) 
            self.rate.sleep() 

if __name__ == '__main__': 
    rospy.init_node('square_holo_node', anonymous=True) 
    sh = SquareHolo() 
    try: 
        sh.move_square() 
    except rospy.ROSInterruptException: 
        Pass 