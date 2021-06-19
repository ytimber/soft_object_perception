import taichi as ti
import numpy as np
import utils
from engine.mpm_solver import MPMSolver

write_to_disk = True
if write_to_disk:
    os.makedirs('outputs', exist_ok=True)

ti.init(arch=ti.cuda)  # Try to run on GPU

gui = ti.GUI("Taichi Elements", res=512, background_color=0x112F41)

mpm = MPMSolver(res=(128, 128))

mpm.add_ellipsoid(center=[0.4, 0.4],
                  radius=[5e-2, 5e-2],
                  material=MPMSolver.material_elastic)
for frame in range(500):
    mpm.step(8e-3)
    if 1<frame < 200:
        mpm.add_cube(lower_corner=[0.1, 0.8],
                     cube_size=[0.01, 0.05],
                     velocity=[1, 0],
                     material=MPMSolver.material_water) 

    if 250 <frame < 400:
        mpm.add_cube(lower_corner=[0.4, 0.8],
                     cube_size=[0.01, 0.05],
                     velocity=[1, 0],
                     material=MPMSolver.material_snow) 
    colors = np.array([0x068587, 0xED553B, 0xEEEEF0, 0xFFFF00],
                      dtype=np.uint32)
    particles = mpm.particle_info()
    gui.circles(particles['position'],
                radius=1.5,
                color=colors[particles['material']])
    gui.show(f'{frame:06d}.png' if write_to_disk else None)
