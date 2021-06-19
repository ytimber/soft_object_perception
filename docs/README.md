# Neural_soft_object_perception
## Basics
Use MLS-MPM solver to simulate water/elastic/snow/sand/mud. Use `render_particles.py` to render the particles. 
To install taichi, use `pip`: `python3 -m pip install taichi`
To run the demo, use `python3 demo/demo_name.py`

## To simulate and render an example 3D scene with Python
1. Make sure you have a modern NVIDIA GPU (e.g. GTX 1080 Ti)
2. run `python3 demo/object_collider_render.py`, a binary file called `sim_xxxx-xx-xx_xx-xx-xx` will be created under the current folder (in this case, `demo`). 
3. To render the particles, run `python3 your/directory/path/engine/render_particles.py your/directory/path/sim_xxxx-xx-xx_xx-xx-xx [begin frame] [end frame] [frame step] [render_output_folder]`
4. Images are now rendered and located in the `[render_output_folder]`
