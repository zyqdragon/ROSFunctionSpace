#include "ros/ros.h"
#include "std_msgs/String.h"
void chatterCallback(const std_msgs::String::ConstPtr& msg)
//是一个回调函数，当接收到 chatter 话题的时候就会被调用。
{ ROS_INFO("I heard: [%s]", msg->data.c_str());
}
int main(int argc, char **argv)
{ ros::init(argc, argv, "listener2");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("testmsg", 1000, chatterCallback);
ros::spin();
return 0; 
}
