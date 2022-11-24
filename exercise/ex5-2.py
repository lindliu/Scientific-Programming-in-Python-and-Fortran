#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:07:50 2022

@author: do0236li
"""

import numpy as np
import matplotlib.pyplot as plt
import perlin2d as pn
import pyvtk as vtk

if __name__ == "__main__":
    ## p47
    noise = pn.generate_perlin_noise_2d((256, 256), (8, 8)).reshape(256*256,).tolist()
    noise_x = pn.generate_perlin_noise_2d((256, 256), (8, 8)).reshape(256*256,1)
    noise_y = pn.generate_perlin_noise_2d((256, 256), (8, 8)).reshape(256*256,1)
    
    vectors = np.hstack((noise_x, noise_y, np.zeros((256*256,1)))).tolist()

    points = vtk.PointData(vtk.Scalars(noise, name='scalar'), vtk.Vectors(vectors, name="vec1"))
    data = vtk.VtkData(vtk.StructuredPoints([256,256]), points)
    data.tofile('p47','ascii')
    
    
    
    ## p48
    import perlin3d as pn

    noise = pn.generate_perlin_noise_3d((64, 64, 64), (8, 8, 8)).reshape(64*64*64,).tolist()
    noise_x = pn.generate_perlin_noise_3d((64, 64, 64), (4, 4, 4)).reshape(64*64*64,1)
    noise_y = pn.generate_perlin_noise_3d((64, 64, 64), (4, 4, 4)).reshape(64*64*64,1)
    noise_z = pn.generate_perlin_noise_3d((64, 64, 64), (4, 4, 4)).reshape(64*64*64,1)
    
    vectors = np.hstack((noise_x, noise_y, noise_z)).tolist()

    points = vtk.PointData(vtk.Scalars(noise, name='scalar'), vtk.Vectors(vectors, name="vec1"))
    data = vtk.VtkData(vtk.StructuredPoints([64,64, 64]), points)
    data.tofile('p48','binary')