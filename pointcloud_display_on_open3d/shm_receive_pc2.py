#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import numpy as np
import open3d as o3d
import time
from multiprocessing import shared_memory
 
# files = os.listdir("pcd2/")
points_num=9984  # points number of pointcloud
frame_num=200  # frame number of merged pointcloud
vis = o3d.visualization.Visualizer()
vis.create_window()
opt = vis.get_render_option()
opt.background_color = np.asarray([0, 0, 0]) 
render_option = vis.get_render_option()
render_option.point_size = 1.0
FOR2 = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5, origin=[0, 0, 0]) 
pointcloud = o3d.geometry.PointCloud()
to_reset = True
vis.add_geometry(pointcloud)
vis.add_geometry(FOR2)
existing_shm = shared_memory.SharedMemory(name='testspace')

idx=1
pcmulti=np.ones([frame_num,points_num,3])
pcmulti=pcmulti.astype("float64")
while(True):
    idx=(idx+1)%20
    print("-----idx=",idx)
    c = np.ndarray((points_num,3), dtype=np.float, buffer=existing_shm.buf)
    c=c.reshape(1,points_num,3)
    # print("-------c=",c)
    # pcd = o3d.io.read_point_cloud("pcd2/" + f)
    # pcd = np.asarray(pcd.points).reshape((-1, 3))
    # print("----pcd[1:3]=",pcd[1:3])
    # pcd=np.array([[idx,1,1],[1,2,3],[2,3,1]])
    #print("shape_c=",c.shape)
    #print("shape_pcmulti=",pcmulti.shape)
    pcmulti=np.concatenate((pcmulti[1:],c),axis=0)
    tpc=pcmulti.reshape(points_num*frame_num,3)
    pcd=tpc
    pointcloud.points = o3d.utility.Vector3dVector(pcd)
    #vis.update_geometry()
    # 注意，如果使用的是open3d 0.8.0以后的版本，这句话应该改为下面格式
    vis.update_geometry(pointcloud)
    if to_reset:
        vis.reset_view_point(True)
        to_reset = False
    time.sleep(0.0001)
    vis.poll_events()
    vis.update_renderer()
