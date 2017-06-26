import numpy.random as nprnd
from timeit import timeit
import sorting
import matplotlib.pyplot as plt
import random


def wrapper(func, *args, **kwargs):
    """for timeit function"""
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def driver(sorting_func, test_size=100, number=10):
    """returns x,y data to test speed of function as input size increases"""
    x = [i for i in range(1, test_size, 3)]
    y = []

    for i in x:
        #rand_arr = nprnd.randint(i, size=i)
        rand_arr = [random.randrange(1, i) for _ in range(1, i)]
        time = timeit(wrapper(sorting_func, rand_arr), number=number)
        print(i, time)
        y.append(time)

    return x, y


def main():
    num = 300  # how many x values u want
    a, b = driver(sorting.fastmergeSort, num)
    c, d = driver(sorting.shellSort, num)
    #e, f = driver(sorting.quickSort, num)
    plt.scatter(a, b)
    plt.scatter(c, d)
    #plt.scatter(e, f)
    plt.show()


def fib(n):
x, y = driver()
