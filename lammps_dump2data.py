from ovito import dataset
from ovito.io import *
from ovito.modifiers import *

# Import a sequence of files.
node = import_file('dump.eqb300K.10000.gz')

# Select all atoms with z coordinate above 22 microns
node.modifiers.append(SelectExpressionModifier(expression = 'Position.Z > 220000.0'))
node.compute()

#Delete Selected particles
mod3=DeleteSelectedParticlesModifier()
node.modifiers.append(mod3)


#Export as a LAMMPS datafile

export_file(node, "data.eqb300K.10000", "lammps_data")
