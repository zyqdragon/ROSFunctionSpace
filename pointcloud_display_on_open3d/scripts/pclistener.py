#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from multiprocessing import shared_memory
from time import sleep
import numpy as np
import os
import time

points_num=9984 # points number of pointcloud
class PointCloudSubscriber(object):
    def __init__(self) -> None:
        #self.sub = rospy.Subscriber("pointcloud_topic",
        self.sub = rospy.Subscriber("livox/lidar2",    # ros topic
                                PointCloud2,
                                self.callback, queue_size=5)
        self.idx=0
    def callback(self, msg):
        assert isinstance(msg, PointCloud2)
        # gen=point_cloud2.read_points(msg,field_names=("x","y","z"))
        points = point_cloud2.read_points_list(
            msg, field_names=("x", "y", "z"))
        #points=points.astype("float")
        #print("---points[0:5]=",points[0:5])
        self.idx=self.idx+1

        # a = np.array([[(self.idx)%5, 3, 6], [points[0][0],points[0][1], points[0][2]]])
        t1=time.time()
        pcd_val=np.array(points)
        #for idx in range(points_num):
        #    a[idx]=np.array([[points[idx][0],points[idx][1], points[idx][2]]])
        print("----time required is:",time.time()-t1)
        #b[:] = a[:]   
        b[:] = pcd_val[:]  
        #b=a
        # print("--dd--new----points=",points)
        # print("----b=",b)
        # sleep(2)
        # print("----points=",len(points))
if __name__ =='__main__':
    rospy.init_node("pointcloud_subscriber")    
    #if not os.path.exists("/smem88"):
    #os.mkdir(training_path)
    # a = np.array([[1, 6, 2],[ 3, 5, 8]])
    a = np.ones([points_num,3])
    a=a.astype("float")
    #idx=0
    shm_a = shared_memory.SharedMemory(create=True,size=a.nbytes,name='testspace')
    b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm_a.buf)
    b[:] = a[:] 
    # b=a
    print("name=",shm_a.name)
    #sleep(1)
    PointCloudSubscriber()
    rospy.spin()
