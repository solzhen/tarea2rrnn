from algoritmo.auxfun import heterogenetic_pop, ez_plot
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IgualdadCondicion, IteracionesCondicion, CombinarCondiciones
from ffuncion.fitnessfunctions import IgualdadNumericString
from gfuncion.generators import binary_gen
import numpy as np

meta = "0010101011010111"
c1 = IgualdadCondicion(len(meta))
c2 = IteracionesCondicion(200)
ci = CombinarCondiciones(c1, c2)
ff = IgualdadNumericString(meta)

heat_map_generation = np.zeros((11,11))

for i in range(11):
	for j in range(11):
		ag = AlgoritmoGenetico(max(i*10,1), ff, binary_gen, 0.1*j, ci, len(meta), heterogenetic_pop)
		ret = ag.run(out=False)
		gen = len(ret)
		heat_map_generation[i][j] = gen

print (heat_map_generation)

import matplotlib.pyplot as plt
import numpy as np
plt.imshow(heat_map_generation, cmap='hot', interpolation='nearest')
plt.show()