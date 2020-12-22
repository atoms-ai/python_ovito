from ovito.io import *
from ovito.data import *
from ovito.modifiers import ExpressionSelectionModifier, DeleteSelectedModifier, ClusterAnalysisModifier
from ovito.pipeline import *
import numpy as np

pipeline = import_file('P1_particle_only.data')

#pipeline.modifiers.append(ClusterAnalysisModifier(cutoff = 2000.0, sort_by_size = True))
data = pipeline.compute()
pos = data.particles.position
#cluster = data.particles.cluster
#for ClusterNum in range(data.attributes['ClusterAnalysis.cluster_count']):

print(np.mean(pos, axis = 0))
