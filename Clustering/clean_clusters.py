# -*- coding: utf-8 -*-
# port of
# http://pointclouds.org/documentation/tutorials/statistical_outlier.php
# you need to download
# http://svn.pointclouds.org/data/tutorials/table_scene_lms400.pcd

import pcl
from  open3d import *
import numpy as np 
from scipy.cluster.vq import kmeans2, whiten
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization!
import pandas as pd


p = pcl.load("./dataset/table_scene_mug_stereo_textured.pcd")

fil = p.make_statistical_outlier_filter()
fil.set_mean_k(50)
fil.set_std_dev_mul_thresh(1.0)

pcl.save(fil.filter(), "./dataset/table_scene_mug_stereo_textured_inliers.pcd")

fil.set_negative(True)
pcl.save(fil.filter(), "./dataset/table_scene_mug_stereo_textured_outliers.pcd")


if __name__ == "__main__":
	pcd = read_point_cloud("./dataset/table_scene_mug_stereo_textured_inliers.pcd")
	draw_geometries([pcd])
	print(pcd)

data = read_point_cloud("./dataset/table_scene_mug_stereo_textured_inliers.pcd")

a = np.asarray(data.points)
fig = plt.figure()
ax = Axes3D(fig)
x, y = kmeans2(whiten(a), 3, iter = 20)
print(x)
print(y)   
ax.scatter(a[:,0], a[:,1], a[:,2], c=y, alpha=0.33333);
fig.savefig('./Results/point_plot_mug_stereo.png')
plt.show()

