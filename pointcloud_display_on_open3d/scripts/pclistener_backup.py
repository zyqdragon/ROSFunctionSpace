#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from multiprocessing import shared_memory
from time import sleep
import numpy as np
import os
class PointCloudSubscriber(object):
    def __init__(self) -> None:
        self.sub = rospy.Subscriber("pointcloud_topic",
                                PointCloud2,
                                self.callback, queue_size=5)
    def callback(self, msg):
        assert isinstance(msg, PointCloud2)
        # gen=point_cloud2.read_points(msg,field_names=("x","y","z"))
        points = point_cloud2.read_points_list(
            msg, field_names=("x", "y", "z"))
        print("---points[0]=",points[0])
        a = np.array([3, 3, 6, points[0][0],points[0][1], points[0][2]])
        b[:] = a[:] 
        print("--dd--new----points=",points)
if __name__ =='__main__':
    rospy.init_node("pointcloud_subscriber")    
    #if not os.path.exists("/smem88"):
    #os.mkdir(training_path)
    a = np.array([1, 6, 2, 3, 5, 8])
    shm_a = shared_memory.SharedMemory(create=True,size=a.nbytes,name='testspace')
    b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm_a.buf)
    b[:] = a[:] 
    print("name=",shm_a.name)
    #sleep(1)
    PointCloudSubscriber()
    rospy.spin()
