import pcl 
from open3d import *
import numpy as np


data = read_point_cloud("./dataset/sac_plane_test.pcd")
draw_geometries([data])
data = pcl.load("./dataset/sac_plane_test.pcd")


cloud = pcl.PointCloud(np.asarray((data), dtype = np.float32))

seg = cloud.make_segmenter_normals(ksearch=50)
seg.set_optimize_coefficients(True)
seg.set_model_type(pcl.SACMODEL_PLANE)
seg.set_normal_distance_weight(0.05)
seg.set_method_type(pcl.SAC_RANSAC)
seg.set_max_iterations(100)
seg.set_distance_threshold(0.005)
inliers, model = seg.segment()

cloud_plane = cloud.extract(inliers, negative=False)
pcl.save(cloud_plane, './Results/sac_plane.pcd')


segment = read_point_cloud('./Results/sac_plane.pcd')


draw_geometries([segment])
