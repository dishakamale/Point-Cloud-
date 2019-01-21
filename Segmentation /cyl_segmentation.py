import pcl
from open3d import *
import numpy as np 

data = pcl.load("./dataset/table_scene_lms400_inliers.pcd")
cloud_cyl = pcl.PointCloud(np.asarray((data), dtype = np.float32))

seg = cloud_cyl.make_segmenter_normals(ksearch=50)
seg.set_optimize_coefficients(True)
seg.set_model_type(pcl.SACMODEL_CYLINDER)
seg.set_normal_distance_weight(0.1)
seg.set_method_type(pcl.SAC_RANSAC)
seg.set_max_iterations(10000)
seg.set_distance_threshold(0.05)
seg.set_radius_limits(0, 0.1)
inliers, model = seg.segment()


cloud_cylinder = cloud_cyl.extract(inliers, negative=False)
pcl.save(cloud_cylinder, './Results/table_scene_mug_textured_cylinder_cyl_segmented_1.pcd')

segment = read_point_cloud('./Results/table_scene_mug_textured_cylinder_cyl_segmented_1.pcd')
draw_geometries([segment])


