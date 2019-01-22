
# PointCloud clustering and segmentation 

The file 'Cluster1.py' clusters the given pointcloud data('table_scene_lms400.pcd') whose results are shown in 'point_plot.png'.

The optimum value of number of clusters is predicted using the elbow method.('Optimal_k.py')

The segmenattion of table-mug cluster is given by 'Segmentation.py'.

'integrate.py' removes the outliers, performs K-means clustering and then uses RANSAC plane and cylinder detection algorithms for segmentation.  



These codes have been tested on Ubuntu 16.04 and python 3.5.2

# Requirements : 

1. numpy = '1.15.4'
2. pandas = '0.23.4'
3. scipy = '1.1.0'
4. matplotlib = '3.0.2'
5. open3d = ''0.4.0.0'
6. mplot3d 
7. pcl = '1.7.2'




