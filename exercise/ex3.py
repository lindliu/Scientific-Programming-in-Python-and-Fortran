#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 16:21:38 2022

@author: dliu
"""

import matplotlib.pyplot as plt
import numpy as np 

# p40
x = np.linspace(-np.pi/3, np.pi/3, 100)

plt.figure(figsize=[10,8])
plt.subplot(2,2,1)
plt.plot(x, np.sin(x))
plt.ylim(-2,2)
plt.title('sin(x)')

plt.subplot(2,2,2)
plt.plot(x, np.cos(x))
plt.ylim(-2,2)
plt.title('cos(x)')

plt.subplot(2,2,3)
plt.plot(x, np.tan(x))
plt.ylim(-2,2)
plt.title('tan(x)')

plt.subplot(2,2,4)
plt.plot(x, np.arctan(x))
plt.ylim(-2,2)
plt.title('acrtan(x)')

# p41
t = np.linspace(-2*np.pi, 2*np.pi)
y = np.sin(t)

plt.figure()
for k in range(3,19,2):
    plt.plot(t,y, label=f'{k-2}')
    y += np.sin(k*t)/k
plt.legend()
plt.title('Square waves')


# p42
x = np.linspace(-np.pi*2, np.pi*2, 100)
y = x.reshape([-1,1])
f = np.sin(x*y/4.0)

fig, ax = plt.subplots(1,2,figsize=[10,8])
contour = ax[0].contour(x, y.flatten(), f, levels=np.linspace(f.min(), f.max(), 10))
# ax[0].clabel(contour, colors = 'k', fmt = '%2.1f', fontsize=12)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')


ax[1].contourf(x, y.flatten(), f, levels=np.linspace(f.min(), f.max(), 10))
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')


# p43
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

x = np.outer(np.linspace(-np.pi*2, np.pi*2, 100), np.ones(100)) 
y = x.copy().T
f = np.sin(x*y/4.0)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, f)












