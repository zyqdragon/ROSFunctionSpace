import open3d as o3d
import numpy as np
from copy import deepcopy

pcd_file="./last_pcd5b.pcd"
#读点云
pcd = o3d.io.read_point_cloud(pcd_file)
points = np.asarray(pcd.points)
#obtain the center of mass by two kinds of codes
center = np.mean(points, axis=0)  
center2= pcd.get_center()
print("---center point 2 is:",center2)
print(pcd)
print(np.asarray(pcd.points))
print("---center is:",center)

# create three coordinate axes in the GUI
FOR1 = o3d.geometry.TriangleMesh.create_coordinate_frame(size=2, origin=[0, 0, 0])
#FOR2 = o3d.geometry.TriangleMesh.create_coordinate_frame(size=3, origin=[0, 0, 0])

# translate the point clouds
pcd.translate((-3.47,1.68,-8.66), relative=True)
#FOR2.translate((5.1,-2,8), relative=True)
# rotate the point clouds
R = pcd.get_rotation_matrix_from_xyz((np.pi/3, np.pi/6, 0))#绕y轴旋转90°
print("----------R=",R,"---type of R=",R.dtype)
pcd.rotate(R, center=True)#旋转点位于x=20处，若不指定则默认为原始点云质心。
pcd.paint_uniform_color([1, 1, 1])#指定显示为蓝色

# o3d.visualization.draw_geometries([FOR1,pcd])

pcddata=pcd.points
points2=np.array([[0,0,0]])
for k in range(len(pcd.points)):
    #if (pcd.points[k][0]<4) and (pcd.points[k][2]>0.1) and (pcd.points[k][2]<10):
    if (pcd.points[k][0]<0.4) and (pcd.points[k][0]>-0.8) and (pcd.points[k][1]<0.8) and (pcd.points[k][1]>-1.1) and (pcd.points[k][2]<0.8) and (pcd.points[k][2]>-1.6):
        print("---len=",len(pcd.points),"---k=",k,"---test point1---",np.array([pcd.points[k]]))
        points2=np.append(points2,np.array([pcd.points[k]]), axis=0)

# transform normal points into radar data
#创建点云对象
pcd=o3d.geometry.PointCloud()
# pcd=o3d.open3d.geometry.PointCloud() 
#将点云数据转换为Open3d可以直接使用的数据类型
pcd.points=o3d.utility.Vector3dVector(points2)
# pcd.points= o3d.open3d.utility.Vector3dVector(raw_point)  # for different opend3d version
# o3d.visualization.draw_geometries([pcd])
o3d.io.write_point_cloud("bucket5.pcd",pcd)#以二进制格式存储点数据集部分

#创建窗口对象
vis = o3d.visualization.Visualizer()
#设置窗口标题
vis.create_window(window_name="kitti")
#设置点云大小
vis.get_render_option().point_size = 1
#设置颜色背景为黑色
opt = vis.get_render_option()
opt.background_color = np.asarray([0, 0, 0])
#将点云加入到窗口中
vis.add_geometry(pcd)
vis.add_geometry(FOR1)
vis.run()
vis.destroy_window()