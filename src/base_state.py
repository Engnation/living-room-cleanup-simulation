#import appopriate dependencies
from pyrobot import Robot

# Create robot.
robot = Robot('locobot')

# Get the current pose of the base i.e, a state of the form (x, y, yaw). Note
# that over here we are querying the 'odom' state, which is state estimated
# from inertial sensors and wheel encoders on the base.
current_state = robot.base.get_state('odom')

# (Advanced) If you are running visual SLAM, then you can also query the state
# as estimated from visual sensors, using the following. State estimates from
# visual SLAM can be more accurate.
current_state = robot.base.get_state('vslam')
