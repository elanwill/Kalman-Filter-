import numpy as np
import math
import matplotlib.pyplot as plt


def fitPoly(x, y, O, graphOut = False):
    if x.size > O+4:
        z = np.polyfit(x,y,O)
        print(z)
    else:
        z = np.zeros(O+1)
        print('y used for fit ', y)
        z[-1] = np.mean(y)

    if graphOut:
        plt.figure()
        p = np.poly1d(z)
        xPlot = np.linspace(x[0], x[-1], 100)

        plt.plot(x, y)
        plt.plot(xPlot, p(xPlot))

    return z

def polyPred(x,y,O, graphOut = False):
    if y.size<2: #if y only 1 value predict same value
        return x
    z = fitPoly(x,y,O, graphOut = False)
    p = np.poly1d(z)
    xPred = 2*x[-1]-x[-2]
    yPred = p(xPred)

    if graphOut:
        plt.figure()
        p = np.poly1d(z)
        xPlot = np.linspace(x[0], xPred, 100)

        plt.plot(x, y)
        plt.plot(xPlot, p(xPlot))
    return yPred

def polyFilter(x,y,O,N):
    yFiltered = np.zeros(x.size)
    for k in range(x.size):
        istart = max([0,k-N])
        yFiltered[k]=polyPred(x[istart:k+1],y[istart:k+1],O)

    return yFiltered
