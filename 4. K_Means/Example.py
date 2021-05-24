from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist 

np.random.seed(11)

means = [[2,2],[8,3],[3,6]]
cov = [[1,0],[0,1]]
N = 500 
X0 = np.random.multivariate_normal(means[0],cov,N)      # Draw random samples from a multivariate normal distribution.
X1 = np.random.multivariate_normal(means[1],cov,N)
X2 = np.random.multivariate_normal(means[2],cov,N)
X = np.concatenate((X0,X1,X2),axis=0)       # axis = 0: join by row, axis = 1: column
K = 3
# print(X.shape)
original_label = np.asarray([0]*N+[1]*N+[2]*N).T        # convert the input to an array
# print(original_label)
def kmeans_display(X,label):    
    K = np.amax(label)+1    # Return the maximum of an array or maximum along an axis.
    X0 = X[label == 0, :]   # original X0, X1, X2 
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    # print(X0,X1,X2)
    plt.plot(X0[:, 0], X0[:, 1], "b^", markersize = 4, alpha =.8)
    plt.plot(X1[:, 0], X1[:, 1], "go", markersize = 4, alpha =.8)
    plt.plot(X2[:, 0], X2[:, 1], "rs", markersize = 4, alpha =.8)

    plt.axis("equal")   
    plt.plot()      # plot the graph with x-axis relative to y-axis
    plt.show()

kmeans_display(X,original_label)