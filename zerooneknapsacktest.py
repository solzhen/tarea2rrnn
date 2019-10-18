from algoritmo.auxfun import heterogenetic_pop, ez_plot
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IteracionesCondicion
from ffuncion.fitnessfunctions import KnapsackValue
from gfuncion.generators import binary_gen

c2 = IteracionesCondicion(200)
weights = [1, 2, 3, 4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15]
values = [5, 8, 10, 12, 15, 20, 20, 21, 25, 30, 33, 35, 35, 35, 48]
ff = KnapsackValue(weights, values, 15)

ag = AlgoritmoGenetico(100, ff, binary_gen, 0.1, c2, len(weights), heterogenetic_pop)

ez_plot(ag.run())