from algoritmo.auxfun import heterogenetic_pop, ez_plot
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IteracionesCondicion
from ffuncion.fitnessfunctions import KnapsackValue
from gfuncion.generators import binary_gen

c2 = IteracionesCondicion(100)
weights = [12, 2, 1, 1, 4]
values = [4, 2, 2, 1, 10]
ff = KnapsackValue(weights, values, 15)

ag = AlgoritmoGenetico(5, ff, binary_gen, 0.1, c2, len(weights), heterogenetic_pop)

ez_plot(ag.run())