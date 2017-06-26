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


def driver(sorting_func, test_size=100, number=100):
    """returns x,y data to test speed of function as input size increases"""
    x = [i for i in range(1, test_size)]
    y = []

    for i in x:
        #rand_arr = nprnd.randint(i, size=i)
        rand_arr = [random.randrange(1, i) for _ in range(1, i)]
        time = timeit(wrapper(sorting_func, rand_arr), number=number)
        print(i, time)
        y.append(time)

    return y


def main():
    num = 1000  # how many x values you want
    quicksort_values = driver(sorting.quickSort, num)
    #bubble_values = driver(sorting.bubble2, num)
    #selection_values = driver(sorting.selection, num)
    #insertion_values = driver(sorting.insertion, num)
    shell_values = driver(sorting.shellSort, num)

    a = [i for i in range(1, num)]

    #plt.scatter(a, bubble_values)
    #plt.scatter(a, selection_values)
    plt.scatter(a, quicksort_values)
    plt.scatter(a, shell_values)

    plt.show()

if __name__ == '__main__':
    main()
