import taichi as ti
import math
import time
import numpy as np
from plyfile import PlyData, PlyElement
import os
import utils
from utils import create_output_folder
from engine.mpm_solver import MPMSolver


with_gui = True
write_to_disk = True
# Try to run on GPU
ti.init(arch=ti.cuda,
        kernel_profiler=True,
        use_unified_memory=False,
        device_memory_fraction=0.7)

max_num_particles = 10000000

if with_gui:
    gui = ti.GUI("MLS-MPM", res=512, background_color=0x112F41)

if write_to_disk:
    output_dir = create_output_folder('/home/yuting/Desktop/taichi_elements-master/demo/sim')

R = 512
mpm = MPMSolver(res=(R, R, R), size=1)

mpm.set_gravity((0, -20, 0))

mpm.add_sphere_collider(center=(0.5, 0.5, 0.5),
                        radius=0.1,
                        surface=mpm.surface_sticky)

mpm.add_ellipsoid(center=[0.5, 0.8,0.5],
                  radius=5e-2,
                  material=MPMSolver.material_elastic)

def visualize(particles):
    np_x = particles['position'] / 1.0

    # simple camera transform
    screen_x = ((np_x[:, 0] + np_x[:, 2]) / 2**0.5) - 0.2
    screen_y = (np_x[:, 1])

    screen_pos = np.stack([screen_x, screen_y], axis=-1)

    gui.circles(screen_pos, radius=0.8, color=particles['color'])
    gui.show()

start_t = time.time()


for frame in range(500):
    print(f'frame {frame}')
    t = time.time()

    mpm.step(2e-3, print_stat=True)
    if with_gui and frame % 3 == 0:
        particles = mpm.particle_info()
        visualize(particles)

    if write_to_disk:
        mpm.write_particles(f'{output_dir}/{frame:05d}.npz')
    print(f'Frame total time {time.time() - t:.3f}')
    print(f'Total running time {time.time() - start_t:.3f}')
