import taichi as ti
import numpy as np
import utils
import os
from engine.mpm_solver import MPMSolver

write_to_disk = True
if write_to_disk:
    os.makedirs('outputs', exist_ok=True)

ti.init(arch=ti.cuda)  # Try to run on GPU

gui = ti.GUI("Taichi Elements", res=512, background_color=0x112F41)

mpm = MPMSolver(res=(64, 64, 64), size=1)

mpm.set_gravity((0, -20, 0))

mpm.add_sphere_collider(center=(0.5, 0.5, 0.5),
                        radius=0.1,
                        surface=mpm.surface_sticky)

mpm.add_ellipsoid(center=[0.5, 0.8,0.5],
                  radius=5e-2,
                  material=MPMSolver.material_elastic)

for frame in range(500):
    mpm.step(8e-3)
    particles = mpm.particle_info()
    np_x = particles['position'] / 1.0

    # simple camera transform
    screen_x = ((np_x[:, 0] + np_x[:, 2]) / 2**0.5) - 0.2
    screen_y = (np_x[:, 1])

    screen_pos = np.stack([screen_x, screen_y], axis=-1)

    gui.circles(screen_pos, radius=1.1, color=particles['color'])
    gui.show(f'outputs/{frame:06d}.png' if write_to_disk else None)
