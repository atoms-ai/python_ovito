# Render

from ovito.io import import_file
from ovito.vis import Viewport, TachyonRenderer
from ovito.modifiers import *

#Import file
pipeline = import_file('../dump.imp_Ra2_Ta850mps.70000')
pipeline.add_to_scene()

#Calculate adaptive CNA
modifier1 = CommonNeighborAnalysisModifier()
pipeline.modifiers.append(modifier1)

# Select atoms to delete
mod2=SelectExpressionModifier()
mod2.expression = '(Position.X < 240000.0)||(Position.X > 260000.0)'
pipeline.modifiers.append(mod2)

#Delete selected atoms
mod3=DeleteSelectedParticlesModifier()
pipeline.modifiers.append(mod3)

#Assign radius to a particle type
types = pipeline.source.data.particles.particle_types
types.type_by_id(1).radius = 1000.00
types.type_by_id(2).radius = 1000.00
types.type_by_id(3).radius = 1000.00
types.type_by_id(4).radius = 1000.00

#Image settings
vp = Viewport(type = Viewport.Type.Ortho, camera_dir = (1, 0, 0))
vp.zoom_all()
vp.render_image(filename='../Ov_Images/dump_70000.png', size=(1920, 1080), renderer=TachyonRenderer())
