import vedo
import numpy as np

class RunnerTest:

    def __init__(self):
        self.positions = np.random.rand(100, 3)
        self.plt = vedo.Plotter(axes=1, interactive=False)
        self.points = vedo.Spheres(self.positions)
        #self.text = vedo.Text2D(c='r4')
        self.plt += [self.points]

    def run(self):
        print("Run simulation...")

        reset_cam = True

        while True:
            self.positions *= 0.99

            self.points.points(self.positions)
            #self.text.text(f'cm={self.points.centerOfMass()}')

            self.plt.show(resetcam=reset_cam)
            if reset_cam:
                reset_cam = False
            if self.plt.escaped:
                break  # if ESC is hit during the loop


rt = RunnerTest()
rt.run()
