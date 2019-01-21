import pcl
from  open3d import *
import numpy as np 
from scipy.cluster.vq import kmeans2, whiten
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 
import pandas as pd


<<<<<<< HEAD
p = pcl.load("./dataset/table_scene_lms400.pcd")
=======
p = pcl.load("./dataset/table_scene_mug_stereo_textured.pcd")
>>>>>>> 8c16ce42546942f1e25aa18870e645beb4461f01

fil = p.make_statistical_outlier_filter()
fil.set_mean_k(50)
fil.set_std_dev_mul_thresh(1.0)

<<<<<<< HEAD
pcl.save(fil.filter(), "./dataset/table_scene_lms400_inliers.pcd")

fil.set_negative(True)
pcl.save(fil.filter(), "./dataset/table_scene_lms400_outliers.pcd")


if __name__ == "__main__":
	pcd = read_point_cloud("./dataset/table_scene_lms400_inliers.pcd")
	draw_geometries([pcd])
	print(pcd)

data = read_point_cloud("./dataset/table_scene_lms400_inliers.pcd")
=======
pcl.save(fil.filter(), "./dataset/table_scene_mug_stereo_textured_inliers.pcd")

fil.set_negative(True)
pcl.save(fil.filter(), "./dataset/table_scene_mug_stereo_textured_outliers.pcd")


if __name__ == "__main__":
	pcd = read_point_cloud("./dataset/table_scene_mug_stereo_textured_inliers.pcd")
	draw_geometries([pcd])
	print(pcd)

data = read_point_cloud("./dataset/table_scene_mug_stereo_textured_inliers.pcd")
>>>>>>> 8c16ce42546942f1e25aa18870e645beb4461f01

a = np.asarray(data.points)
fig = plt.figure()
ax = Axes3D(fig)
x, y = kmeans2(whiten(a), 3, iter = 20)
print(x)
print(y)   
ax.scatter(a[:,0], a[:,1], a[:,2], c=y, alpha=0.33333);
fig.savefig('./Results/point_plot_mug.png')
plt.show()

