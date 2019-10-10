import numpy as np


def heterogenetic_pop(n, l, gf):
    return np.array([
        np.array([
            gf() for i in range(l)
        ]) for j in range(n)
    ])