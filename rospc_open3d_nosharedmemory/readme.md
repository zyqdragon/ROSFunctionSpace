# Notice:
pclistener.py读取ros空间中的点云数据，并通过open3d库文件进行直接的可视化显示，不需要通过共享内存来传输数据。其中有两个参数需要设置：  
1. points_num=9984 # points number of pointcloud  
这个参数值根据代码中print("----points_num=",len(points))语句输出的points_num值来确定。
2. frame_num=20  # frame number of merged pointcloud；  
这个参数值代表需要叠加的点云的帧数。需要根据实际的需求来设置。
