import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from open3d import *
from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization!
from scipy.cluster.vq import kmeans2, whiten
import pptk 
%matplotlib inline



data = read_point_cloud("./dataset/table_scene_lms400.pcd")

a = np.asarray(data.points)
fig = plt.figure()
ax = Axes3D(fig)
x, y = kmeans2(whiten(a), 6, iter = 20)


v = pptk.viewer(a)
ax.scatter(a[:,0], a[:,1], a[:,2], c=y, alpha=0.33333);

plt.show()





i=1;
c_1= np.zeros((460000,3));
c_2= np.zeros((460000,3));
c_3= np.zeros((460000,3));

for i in range (1,460000) :
    if (y[i]==0):
        c_1[i,:] = a[i,:];
        #print("condition satisfied")
    
    if (y[i]==1):
        c_2[i,:] = a[i,:];
        
    if (y[i]==2):
        c_3[i,:] = a[i,:];
        
        

fig1 = plt.figure()
axc_1 = Axes3D(fig1)
axc_1.scatter(c_1[:,0],c_1[:,1],c_1[:,2],c='yellow', alpha=0.33333)



fig2 = plt.figure()
axc_2 = Axes3D(fig2)
axc_2.scatter(c_2[:,0],c_2[:,1],c_2[:,2],c='red', alpha=0.33333)
fig2.savefig('./Results/point_plot_segmented.png')
v1 = pptk.viewer(c_2,rgb)


fig3 = plt.figure()
axc_3 = Axes3D(fig3)
axc_3.scatter(c_3[:,0],c_3[:,1],c_3[:,2],c='blue', alpha=0.33333)

