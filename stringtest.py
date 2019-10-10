import numpy as np

from algoritmo.auxfun import heterogenetic_pop, ez_plot
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IgualdadCondicion, IteracionesCondicion, CombinarCondiciones
from ffuncion.fitnessfunctions import IgualdadString
from gfuncion.generators import ordinal_alphabet_gen

meta = "Hello World!"
c1 = IgualdadCondicion(len(meta))
c2 = IteracionesCondicion(1000)
ci = CombinarCondiciones(c1, c2)
ff = IgualdadString(meta)
ag = AlgoritmoGenetico(100, ff, ordinal_alphabet_gen, 0.2, ci, len(meta), heterogenetic_pop)

ez_plot(ag.run())
