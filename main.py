from curve1D import *
from polyFilter import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dt = 0.01
    T = 10
    ex = 0.05
    tvec, x, v, a = drawCurve(T, dt)
    xM = measure(x, ex)

    z = 9
    #q = polyPred(tvec[:z],xM[:z],2, graphOut = True)

    xPolyFiltered, vPoly = polyFilter(tvec, xM,2,10)

    print('std measurement ', np.std(xM-x))
    print('std polypredict ', np.std(xPolyFiltered-x))

    plt.figure()
    plt.plot(tvec, x)
    plt.plot(tvec, xM)
    plt.plot(tvec, xPolyFiltered)
    #plt.plot(tvec, vPoly)
    #plt.plot(tvec, xPolyFiltered-xM)
    plt.show()
