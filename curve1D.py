import numpy as np
import math
import matplotlib.pyplot as plt



def drawCurve(T, dt):
    tvec = np.arange(0,T,dt)
    x = np.zeros(tvec.size)
    x[tvec<2]=tvec[tvec<2]*0.5
    x[(tvec >= 2) * (tvec < 4)] = 1
    x[tvec>=4]                  = np.cos(2*(tvec[tvec>=4]-4))

    v = np.zeros(tvec.size)
    v[tvec < 2]                 = 0.5
    v[(tvec >= 2) * (tvec < 4)] = 0
    v[tvec >= 4]                = -np.sin(2*(tvec[tvec>=4]-4))

    a = np.zeros(tvec.size)
    a[tvec < 2] = 0
    a[(tvec >= 2) * (tvec < 4)] = 0
    a[tvec >= 4]                = -np.cos(2*(tvec[tvec>=4]-4))

    return tvec, x, v, a

def measure(x, ex):
    return x+np.random.normal(0, ex, x.size)


if __name__ == '__main__':
    dt = 0.01
    T = 10
    ex = 0.01
    tvec, x, v, a = drawCurve(T, dt)
    xM = measure(x, ex)

    plt.figure()
    plt.plot(tvec, x)
    plt.plot(tvec, xM)
    plt.plot(tvec, v)
    plt.plot(tvec, a)

    plt.show()
