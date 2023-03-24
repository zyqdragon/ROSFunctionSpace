# memory
rosbag play-l basic_pcd.bag
pclistener.py代码读取ros空间中的点云数据，然后通过共享内存发送至shm_receive_pc2.py代码中并通过open3d进行实时点云数据的显示。
注意：pclistener.py中需要调整点云的点数这个参数：
points_num=9984 # points number of pointcloud
点云的点数参数可以通过pclistener.py中的# print("----points=",len(points))语句获得。
