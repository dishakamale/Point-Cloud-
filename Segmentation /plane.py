import pcl 
from open3d import *
import numpy as np

data = pcl.load("/home/dishuuuuu/pcl-1.7.2/test/sac_plane_test.pcd")

print("yeay")

a = pcl.PointCloud(np.asarray((data), dtype = np.float32))
seg = a.make_segmenter()
seg.set_model_type(pcl.SACMODEL_PLANE)
seg.set_method_type(pcl.SAC_RANSAC)
indices, model = seg.segment()

print("and it is done!")
