import open3d as o3d
import numpy as np

# 加载点云
pcd = o3d.io.read_point_cloud("./bucket5.pcd")
#o3d.visualization.draw_geometries([pcd])
print("Downsample the point cloud with a voxel of 0.02")

print("Radius oulier removal")
cl, ind = pcd.remove_radius_outlier(nb_points=20, radius=0.05)
print("----cl=",cl)
#print("---ind",ind)
# display_inlier_outlier(pcd, ind)

o3d.io.write_point_cloud("./bucket5b.pcd",cl)#以二进制格式存储点数据集部分

#创建窗口对象
vis = o3d.visualization.Visualizer()
#设置窗口标题
vis.create_window(window_name="kitti")
#设置点云大小
vis.get_render_option().point_size = 2
#设置颜色背景为黑色
opt = vis.get_render_option()
opt.background_color = np.asarray([0, 0, 0])
#将点云加入到窗口中
vis.add_geometry(cl)
vis.run()
vis.destroy_window()

# # 统计滤波
# num_neighbors = 80  # K邻域点的个数
# std_ratio = 2.0  # 标准差乘数
# # 执行统计滤波，返回滤波后的点云sor_pcd和对应的索引ind
# sor_pcd, ind = pcd.remove_statistical_outlier(num_neighbors, std_ratio)
# sor_pcd.paint_uniform_color([0, 0, 1])
# print("统计滤波后的点云：", sor_pcd)
# sor_pcd.paint_uniform_color([0, 0, 1])
# # 提取噪声点云
# sor_noise_pcd = pcd.select_by_index(ind, invert=True)
# print("噪声点云：", sor_noise_pcd)
# sor_noise_pcd.paint_uniform_color([1, 0, 0])
# # 可视化滤波结果
# #o3d.visualization.draw_geometries([sor_pcd, sor_noise_pcd], window_name="统计滤波",
# #                                  width=800,  # 窗口宽度
# #                                  height=600)  # 窗口高度

# o3d.visualization.draw_geometries(sor_pcd, window_name="统计滤波",
#                                   width=800,  # 窗口宽度
#                                   height=600)  # 窗口高度
