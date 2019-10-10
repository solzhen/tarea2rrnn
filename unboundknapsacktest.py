from algoritmo.auxfun import heterogenetic_pop, ez_plot
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IteracionesCondicion
from ffuncion.fitnessfunctions import KnapsackValue
from gfuncion.generators import integer_ten_gen

c2 = IteracionesCondicion(200)
weights = [12, 2, 1, 1, 4]
values = [7, 2, 2, 1, 10]
ff = KnapsackValue(weights, values, 15)

ag = AlgoritmoGenetico(100, ff, integer_ten_gen, 0.2, c2, 5, heterogenetic_pop)

ez_plot(ag.run())