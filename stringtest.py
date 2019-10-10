import numpy as np

from algoritmo.auxfun import heterogenetic_pop
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IgualdadCondicion, IteracionesCondicion, CombinarCondiciones
from ffuncion.string import IgualdadString
from gfuncion.alphabet import ordinalgen

meta = "Hello World!"
c1 = IgualdadCondicion(len(meta))
c2 = IteracionesCondicion(1000)
ci = CombinarCondiciones(c1, c2)
ff = IgualdadString(meta)
ag = AlgoritmoGenetico(100, ff, ordinalgen, 0.1, ci, len(meta), heterogenetic_pop)
ret = ag.run()

import matplotlib.pyplot as plt

f1 = plt.figure(1)
ax1 = f1.add_subplot(111);
ax1.set_title("Gen Alg")
ax1.set_xlabel('Generation')
ax1.set_ylabel('Score')
ax1.plot(ret[:, 0], c='r', label='Max Score')
ax1.plot(ret[:, 1], c='b', label='Average Score')
ax1.plot(ret[:, 2], c='g', label='Min Score')
ax1.legend()
f1.show()