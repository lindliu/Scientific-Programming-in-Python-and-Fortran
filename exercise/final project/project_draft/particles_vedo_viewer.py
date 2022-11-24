#!/usr/bin/env python

import sys

from vedo import Plotter, Cube, Sphere, Spheres, Box, mag2, versor, vector, settings
from vedo.pointcloud import Points

# from particle import *
import numpy as np


class Particles_state:
    def __init__(self, filename=""):
        self.filename = filename
        self.steps = 0
        
    def read(self):
        self._particleDict = []
        self._particles = []
        self._particleRadius = []
        with open(self.filename, 'r') as infile:
            nParticles = int(next(infile))
            for _ in range(nParticles):
                line = next(infile)
                line_ = line.strip().split(' ')
                line_ = [float(i) for i in line_ if i!='']
                # print(line_, len(line_))
                
                self._particleRadius.append(line_)
            
            for line in infile:
                line_ = line.strip().split(' ')
                line_ = [float(i) for i in line_ if i!='']
                # print(line_, len(line_))
                
                if len(line_)>1:
                    self._particles.append(line_)
                
                if len(line_)==1:
                    self._particleDict.append(self._particles)
                    self._particles = []
            
        self._particleRadius = np.array(self._particleRadius).flatten()
        self._particleDict = np.array(self._particleDict[1:])

# path = './src/build-particles-Desktop_Qt_5_15_2_MinGW_64_bit-Debug/particle.state'
# _particles = Particles_state(path)
# _particles.read()


class Particle:
    """
    Class implementing a single particle. Uses a vedo Sphere to represent the particle.
    """

    def __init__(self, plt, pos, radius=0.1, color='gray', res=8, use_trail=False):
        """Class constrcutor
        
        Initialises variables and creates a vedo Sphere object attribute and adds
        it to the vedo plotter object.
        """
        self.__pos = pos
        self.__plt = plt
        self.__r = radius
        self.__color = 'gray'
        self.__res = res
        self.use_trail = use_trail

        self.vsphere = Sphere(self.__pos, r=self.__r,
                              c=self.__color, res=self.__res)

        if self.use_trail:
            # self.vsphere.addTrail(alpha=1, maxlength=1, n=50, c="g")
            self.vsphere.add_trail(alpha=1, maxlength=1, n=50, c="g")

        self.__plt.add(self.vsphere, render=False)

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos
        self.vsphere.pos(self.__pos)

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        self.__r = r

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def res(self):
        return self.__res

    @res.setter
    def res(self, res):
        self.__res = res


class Particles:
    """
    Class implementing a set of Particle objects. Contains methods for 
    updating all particles from the positions and sizes arrays.
    """

    def __init__(self, plt, positions, sizes):
        self.__positions = positions
        self.__sizes = sizes
        self.__plt = plt

        self.__particles = []
        for pos, size in zip(self.__positions, self.__sizes):
            self.__particles.append(Particle(self.__plt, pos, size, plt))
            # print(Particle(self.__plt, pos, size, plt).pos)

    def update(self, pos):
        """Updates the sphere particles with positions from the positions array."""
        for i, p in enumerate(self.__particles):
            # p.pos = self.__positions[i]
            p.pos = pos[i]
            
# plt = Plotter(title="Particle Simulator",
#               bg="black", axes=0, interactive=False)

# # aa_ = Particle(plt, _particles._particleDict[0], radius=_particles._particleRadius)

# aa = Particles(plt, _particles._particleDict[0], _particles._particleRadius)


class ParticleViewer:
    """
    A class to manage a particle simulation. 
    """

    def __init__(self, data, plt=None):
        """ParticleSimulation constructor
        
        Initalises default values and initialises the particles system.
        """
        
        self._particleDict = data._particleDict
        self._particleRadius = data._particleRadius
        self.__plt = plt
        self.__initialised = False
        self.__particles = None

        self.__init_system()

    def __init_system(self):
        """Initialises the particles system and calls the fortran extension modules."""

        # if self.initialised:
        #     particle_driver.deallocate_system()

        # self.__positions = np.zeros([self.n_particles, 3], 'd', order='F')        
        # self.__sizes = np.zeros([self.n_particles], 'd', order='F')

        print("Initialise system...")
        self.__positions = self._particleDict[0]
        self.__sizes = self._particleRadius
        
        # particle_driver.init_system(
        #     self.__n_particles, self.__r_min, self.__r_max, self.__v_min, self.__v_max)
        # particle_driver.get_sizes(self.__sizes)
        # particle_driver.get_positions(self.__positions)

        self.__particles = Particles(
            self.__plt, self.__positions, self.__sizes)

        self.initialised = True

    def run(self):
        """Runs the actual simulations.
        
        The method returns when ESC has been pressed.
        """

        print("Run simulation...")

        reset_cam = True

        # while True:
        for j in range(1,1000):
            # particle_driver.collision_check()
            # particle_driver.boundary_check()
            # particle_driver.update()
            # particle_driver.get_positions(self.__positions)
            
            ####################
            self.__positions = self._particleDict[j]
            # print(self.__positions)
            ####################
            
            self.__particles.update(self.__positions)
            
            self.__plt.show(resetcam=reset_cam, axes=1)

            if reset_cam:
                reset_cam = False
            if plt.escaped:
                break  # if ESC is hit during the loop

    # def __del__(self):
    #     """Destructor
        
    #     Asks the fortran extension module to deallocate memory."""

    #     print("End simulation...")

    #     particle_driver.deallocate_system()
    def update(self):
        """Updates the sphere particles with positions from the positions array."""
        for i, p in enumerate(self.__particles):
            p.pos = self.__positions[i]
            
    @property
    def n_particles(self):
        return self.__n_particles

    @n_particles.setter
    def n_particles(self, n):
        self.__n_particles = n
        self.__init_system()

    @property
    def r_min(self):
        return self.__r_min

    @r_min.setter
    def r_min(self, v):
        self.__r_min = v
        self.__init_system()

    @property
    def r_max(self):
        return self.__r_max

    @r_max.setter
    def r_max(self, v):
        self.__r_max = v
        self.__init_system()

    @property
    def v_min(self):
        return self.__v_min

    @v_min.setter
    def v_min(self, v):
        self.__v_min = v
        self.__init_system()

    @property
    def v_max(self):
        return self.__v_max

    @v_max.setter
    def v_max(self, v):
        self.__v_max = v
        self.__init_system()

    @property
    def plt(self):
        return self.__plt

    @plt.setter
    def plt(self, plt):
        self.__plt = plt

    @property
    def initialised(self):
        return self.__initialised

    @initialised.setter
    def initialised(self, flag):
        self.__initialised = flag


if __name__ == "__main__":

    settings.use_depth_peeling = False

    ####### load data ########
    path = './src/build-particles-Desktop_Qt_5_15_2_MinGW_64_bit-Debug/particle.state'
    _particles = Particles_state(path)
    _particles.read()

    ####### view the simulation by Fortran #######
    plt = Plotter(title="Particle Simulator",
                  bg="black", axes=0, interactive=False)
    part_sys = ParticleViewer(_particles, plt)
    part_sys.run()

    plt.show(interactive=True, resetcam=False).close()
