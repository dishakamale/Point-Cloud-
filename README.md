
# Project Overview  

This work focuses on 3D visualization of the given point cloud data. The goal of this project is to enable the user to select a desired object from the given point cloud which will be highlighted in the GUI.  

The four main parts are :
1. Filtering 
2. Segmentation (*RANSAC*)
3. Clustering (*K-means*)
4. Visualization (*RVIZ*)


These codes have been tested on **Ubuntu 16.04** and **python 3.5.2** and **ros - kinetic**

## Requirements : 

1. numpy = '1.15.4'
2. pandas = '0.23.4'
3. scipy = '1.1.0'
4. matplotlib = '3.0.2'
5. open3d = ''0.4.0.0'
6. pcl = '1.7.2' 
7. mplot3d



## Installation :

1. Create and source a virtual environment for python3
```
 $ sudo apt install python3-virtualenv
 $ virtualenv -p python3 --no-site-packages <path to env>
 $ source <path>/bin/activate
```

2. Install the required packages and libraries. 
```
 $ pip install numpy scipy pandas 

 $ sudo apt-get install python3-matplotlib
```
3. Open3d installation. 
```
 $ pip install open3d-python
```
4. python-pcl installation. 

 [Instructions for installation](https://docs.google.com/document/d/1hDSsDuJrm9zsK83CwWAG3MFCBzwxO3FevBTzDMlx1qk/edit?usp=sharing)
