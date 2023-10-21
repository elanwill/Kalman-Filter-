from curve1D import *
from polyFilter import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dt = 0.01
    T = 10
    ex = 0.01
    tvec, x, v, a = drawCurve(T, dt)
    xM = measure(x, ex)

    z = 9
    #q = polyPred(tvec[:z],xM[:z],2, graphOut = True)

    xPolyFiltered, vPoly, aPoly = polyFilter(tvec, xM,2,40)

    plt.figure()
    plt.plot(tvec, x)
    plt.plot(tvec, xM)
    plt.plot(tvec, xPolyFiltered)
    plt.plot(tvec, vPoly)
    plt.plot(tvec, aPoly/2)
    #plt.plot(tvec, xPolyFiltered-xM)
    plt.show()
