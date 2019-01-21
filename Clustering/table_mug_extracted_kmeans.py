import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from open3d import *
from mpl_toolkits.mplot3d import axes3d, Axes3D
from scipy.cluster.vq import kmeans2, whiten


data = read_point_cloud("./Results/extracted_table_mug.pcd")

a = np.asarray(data.points)

fig = plt.figure()
ax = Axes3D(fig)
x, y = kmeans2(whiten(a), 2, iter = 20)
print(x)
print(y)   
ax.scatter(a[:,0], a[:,1], a[:,2], c=y, alpha=0.33333);
fig.savefig('./Results/point_plot_mug_table_final.png')
plt.show()


