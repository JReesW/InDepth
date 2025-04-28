import matplotlib.pyplot as plt
import numpy as np

from math import pi, sin
from mothic.maths.numbers import remap


def lissajous(anchor: tuple[int, int], width, height, n, m, t, total):
    theta = remap(t, 0, total, 0, 2 * pi)
    dx = width * sin(n * theta)
    dy = height * sin(m * theta)
    x, y = anchor
    return x + dx, y + dy


if __name__ == '__main__':
    A = 300
    B = 800
    C = 4

    N = 3
    M = 2
    #
    # ax = plt.figure().add_subplot(projection='3d')
    #
    # # Prepare arrays x, y, z
    # theta = np.linspace(0, 2 * np.pi, 100)
    # x = A * np.sin(theta)
    # y = B * np.sin(N * theta)
    # z = C * np.sin(M * theta)
    #
    # ax.set_xlim([-A, A])
    # ax.set_ylim([-B, B])
    # ax.set_zlim([-C, C])
    # ax.plot(x, y, z, label='parametric curve')
    # ax.legend()
    #
    # plt.show()