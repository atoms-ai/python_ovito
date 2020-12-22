# -*- coding: utf-8 -*-

from ovito.io import import_file, export_file
from ovito.modifiers import *

node = import_file("dump.02000")

modifier=AtomicStrainModifier()
modifier.reference.load("../dump.000001")


#Cutoff should account for 3 neighbor shells, for fcc that is 1.225 times a, Here we use L512 lattice constant of aluminum (QCGD)
modifier.cutoff=2600.0

#modifier.output_deformation_gradients=True
#modifier.output_nonaffine_squared_displacements=True
modifier.output_strain_tensors=True

#Calculate Atomic strains
node.modifiers.append(modifier)

modifier1 = CommonNeighborAnalysisModifier()
node.modifiers.append(modifier1)


# Select all atoms with z above 45 microns: section of 6.4 um as in 2D analysis

mod2=SelectExpressionModifier()
mod2.expression = '(Position.Z < 450000)||(Position.X < 218000)||(Position.X > 282000)'

node.modifiers.append(mod2)

mod3=DeleteSelectedParticlesModifier()

node.modifiers.append(mod3)



export_file(node, 'strain.02000', 'lammps_dump',columns = ['Particle Identifier', 'Particle Type', 'Position.X', 'Position.Y', 'Position.Z', 'Structure Type',\
	 'Strain Tensor.XX', 'Strain Tensor.YY', 'Strain Tensor.ZZ', 'Strain Tensor.XY', 'Strain Tensor.XZ', 'Strain Tensor.YZ', 'Shear Strain', 'Volumetric Strain'])
###	 'Deformation Gradient.11', 'Deformation Gradient.21', 'Deformation Gradient.31', 'Deformation Gradient.12', 'Deformation Gradient.22', 'Deformation Gradient.32', 'Deformation Gradient.13', 'Deformation Gradient.23', 'Deformation Gradient.33'])

