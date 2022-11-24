# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:53:05 2022

@author: jo6815en
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


path_size = './src/build-particles-Desktop_Qt_5_15_2_MinGW_64_bit-Debug/particle.state'

data_size = []
data = []
data_batch = []
with open(path_size, 'r') as infile:
    dim = int(next(infile))
    for _ in range(dim):
        line = next(infile)
        line_ = line.strip().split(' ')
        line_ = [float(i) for i in line_ if i!='']
        print(line_, len(line_))

        data_size.append(line_)
    
    for line in infile:
        line_ = line.strip().split(' ')
        line_ = [float(i) for i in line_ if i!='']
        print(line_, len(line_))

        if len(line_)>1:
            data_batch.append(line_)
        
        if len(line_)==1:
            data.append(data_batch)
            data_batch = []
            
data_size = np.array(data_size)*1000
data = np.array(data[1:])



# plt.plot(data[:,5,:])


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# # for i in range(10):
# #     ax.plot(data[:,i,0], data[:,i,1], data[:,i,2])
    
# def update(num, data, line):
#     line.set_data(data[:2, :num])
#     line.set_3d_properties(data[2, :num])
    
# N = data.shape[0]
# j = 1
# data_ = data[:,j,:].T
# line, = ax.plot(data_[0, 0:1], data_[1, 0:1], data_[2, 0:1])

# # Setting the axes properties
# ax.set_xlim3d([0.0, 1.0])
# ax.set_xlabel('X')

# ax.set_ylim3d([0.0, 1.0])
# ax.set_ylabel('Y')

# ax.set_zlim3d([0.0, 10.0])
# ax.set_zlabel('Z')

# ani = FuncAnimation(fig, update, N, fargs=(data_, line), interval=10000/N, blit=False)



# data = data[:,:10,:]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# for i in range(10):
#     ax.plot(data[:,i,0], data[:,i,1], data[:,i,2])
    
def update(num, data, scatters):
    for i in range(data[0].shape[0]):
        scatters[i]._offsets3d = (data[num][i,0:1], data[num][i,1:2], data[num][i,2:])
    return scatters
    
N = data.shape[0]
scatters = [ ax.scatter(data[0][i,0:1], data[0][i,1:2], data[0][i,2:], s=data_size[i]) for i in range(data[0].shape[0]) ]

# Setting the axes properties
ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 1.0])
ax.set_zlabel('Z')

ani = FuncAnimation(fig, update, N, fargs=(data, scatters), interval=.001, blit=False)




