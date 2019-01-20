import pcl
from  open3d import *
import numpy as np 
from scipy.cluster.vq import kmeans2, whiten


p = pcl.load("./dataset/table_scene_lms400.pcd")

fil = p.make_statistical_outlier_filter()
fil.set_mean_k(50)
fil.set_std_dev_mul_thresh(1.0)

pcl.save(fil.filter(), "./dataset/table_scene_lms400_inliers.pcd")

fil.set_negative(True)
pcl.save(fil.filter(), "./dataset/table_scene_lms400_outliers.pcd")

