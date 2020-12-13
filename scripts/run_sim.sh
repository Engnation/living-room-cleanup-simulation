#!/bin/bash

export GAZEBO_MODEL_PATH=~/catkin_ws/src/living_room_sim_1/models:~/.gazebo/models:${GAZEBO_MODEL_PATH}
export ROS_PACKAGE_PATH="/home/$USER/catkin_ws/src:/home/$USER/low_cost_ws/src:/opt/ros/melodic/share"

source ~/catkin_ws/devel/setup.bash

#This bash script loads the living room cleanup simulation

roslaunch locobot_gazebo gazebo_moveit_main.launch # &

#"$@"
#exec "$SHELL"# -e /home/$USER/catkin_ws/src/living_room_sim_1/scripts detector.sh"

#sleep 15
#gnome-terminal -e home/$USER/catkin_ws/src/living_room_sim_1/scripts detector.sh
#x-terminal-emulator -x /home/$USER/catkin_ws/src/living_room_sim_1/scripts detector.sh
#$TERM -e home/$USER/catkin_ws/src/living_room_sim_1/scripts detector.sh

#give Gazebo and RViz some time to load
#sleep 30
#source ~/catkin_ws/devel/setup.bash

#roslaunch darknet_ros yolo_v3.launch & 

#gnome-terminal
#x-terminal-emulator -e rqt

#rqt



#source /opt/ros/melodic/setup.bash



#export ORBSLAM2_LIBRARY_PATH=/home/$USER/low_cost_ws/src/pyrobot/robots/LoCoBot/install/../thirdparty/ORB_SLAM2
#source /home/$USER/low_cost_ws/devel/setup.bash
#alias load_pyrobot_env='source /home/$USER/pyenv_pyrobot_python3/bin/activate && source /home/$USER/pyrobot_catkin_ws/devel/setup.bash'
