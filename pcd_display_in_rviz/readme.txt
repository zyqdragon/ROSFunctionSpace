
# create the function package
catkin_create_pkg pcd_to_rviz pcl_conversions pcl_ros roscpp sensor_msgs;

pointcloud pcd file is displayed in the rviz.
在一个新的终端中运行roscore
在运行source命令的终端中运行rosrun pcd_to_rviz pcd_to_rviz
在一个新终端中运行rviz命令
rviz打开后，手动加载PointCloud2
PointCloud2中的Topic改为pcl_output1
Global Options中的Fixed Frame改为odom1
即可看到pcd文件中的点云
