import numpy as np


def heterogenetic_pop(n, l, gf):
    return np.array([
        np.array([
            gf() for i in range(l)
        ]) for j in range(n)
    ])


def ez_plot(ret):
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