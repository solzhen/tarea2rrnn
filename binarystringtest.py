from algoritmo.auxfun import heterogenetic_pop
from algoritmo.genetico import AlgoritmoGenetico
from condicion.condicion import IgualdadCondicion, IteracionesCondicion, CombinarCondiciones
from ffuncion.string import IgualdadNumericString
from gfuncion.binary import normalgen

meta = "00101010110101"
c1 = IgualdadCondicion(len(meta))
c2 = IteracionesCondicion(100)
ci = CombinarCondiciones(c1, c2)
ff = IgualdadNumericString(meta)
ag = AlgoritmoGenetico(100, ff, normalgen, 0.1, ci, len(meta), heterogenetic_pop)
ret = ag.run()