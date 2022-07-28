#include <sstream>
#include "ros/ros.h"
#include "std_msgs/String.h"

int main(int argc, char **argv){
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
  ros::Publisher testmsg_pub = n.advertise<std_msgs::String>("testmsg", 1000);
  ros::Rate loop_rate(10);
  /* a unique string for each message.  */
  int count = 0;
  while (ros::ok()) //ros::ok()
  {
     std_msgs::String msg,msg1;
     std::stringstream ss,ss1;

     ss << "\nhello world, I am a genius! " << count;
     msg.data = ss.str();
     ROS_INFO("%s", msg.data.c_str());
     chatter_pub.publish(msg);

     ss1<< "\nTest Message, Please Reply! " << count;
     msg1.data = ss1.str();
     ROS_INFO("%s", msg1.data.c_str());
     testmsg_pub.publish(msg1);

     ros::spinOnce();
     loop_rate.sleep();
     ++count;
  }
return 0;}
