#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from time import sleep
import numpy as np
import os
import time
import open3d as o3d

points_num=9984 # points number of pointcloud
frame_num=20  # frame number of merged pointcloud

class PointCloudSubscriber(object):
    def __init__(self) -> None:
        #self.sub = rospy.Subscriber("pointcloud_topic",
        self.sub = rospy.Subscriber("livox/lidar2",    # ros topic
                                PointCloud2,
                                self.callback, queue_size=5)
        self.idx=1
        self.pcmulti=np.ones([frame_num,points_num,3])
        self.pcmulti=self.pcmulti.astype("float64")
        self.to_reset=True
    def callback(self, msg):
        assert isinstance(msg, PointCloud2)
        # gen=point_cloud2.read_points(msg,field_names=("x","y","z"))
        points = point_cloud2.read_points_list(
            msg, field_names=("x", "y", "z"))
        print("----points_num=",len(points))
        self.idx=(self.idx+1)%20
        print("-----idx=",self.idx)
        t1=time.time()
        pcd_val=np.array(points)
        pcd_val=pcd_val.reshape(1,points_num,3)
        self.pcmulti=np.concatenate((self.pcmulti[1:],pcd_val),axis=0)
        tpc=self.pcmulti.reshape(points_num*frame_num,3)
        print("----time required is:",time.time()-t1)
        pointcloud.points = o3d.utility.Vector3dVector(tpc)
        vis.update_geometry(pointcloud)
        if self.to_reset:
            vis.reset_view_point(True)
            self.to_reset = False
        time.sleep(0.0001)
        vis.poll_events()
        vis.update_renderer()
if __name__ =='__main__':
    rospy.init_node("pointcloud_subscriber")    
    # points_num=9984  # points number of pointcloud
    # frame_num=200  # frame number of merged pointcloud
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    opt = vis.get_render_option()
    opt.background_color = np.asarray([0, 0, 0]) 
    render_option = vis.get_render_option()
    render_option.point_size = 1.0
    FOR2 = o3d.geometry.TriangleMesh.create_coordinate_frame(size=2, origin=[0, 0, 0]) 
    pointcloud = o3d.geometry.PointCloud()
    vis.add_geometry(pointcloud)
    vis.add_geometry(FOR2)
    PointCloudSubscriber()
    rospy.spin()