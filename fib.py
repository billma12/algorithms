import time
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
from numpy.random import normal, rand
import sympy as sympy
from scipy.optimize import curve_fit

# calculates the nth fib term


def fib(n):
    if n < 1:
        return 0
    if n is 1:
        return 1

    return fib(n - 2) + fib(n - 1)


def main():
    res = []
    n = 30

    for i in range(n):
        start_time = time.time()
        fib(i)
        end_time = round(time.time() - start_time, 3)
        res.append(end_time)

    for item in enumerate(res):
        print(item)

# plot code below

    a = [i for i in range(n)]
    b = res
    plt.plot(a, b)

    def func(x, a, b):
        return a * np.exp(b * x)

    x = np.array(a, dtype=float)
    y = np.array(b, dtype=float)

    popt, pcov = curve_fit(func, x, y)

    print(popt[0], popt[1])
    plt.plot(a, func(x, *popt))
    plt.show()

main()
