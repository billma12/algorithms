from timeit import timeit
import matplotlib.pyplot as plt


def driver(func, test_size=100, number=10):
    """returns x,y data to test speed of function as input size increases"""
    def wrapper(func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped

    x = [i for i in range(1, test_size)]
    y = []

    for i in x:
        time = timeit(wrapper(func, i), number=number)
        print(i, time)
        y.append(time)

    return x, y


def f(x):
    if x < 2:
        return 1
    return x * f(x - 1)


def fact(n):
    return fact_help(1, n)


def fact_help(product, n):
    if n == 1:
        return product
    return fact_help(product * n, n - 1)


def fib(x):
    if x < 2:
        return 1
    return fib(x - 1) + fib(x - 2)

memo = {}


def fib_memo(x):
    if x in memo:
        return memo[x]
    if x < 2:
        return 1
    else:
        f = fib_memo(x - 1) + fib_memo(x - 2)
    memo[x] = f
    return f

x, y = driver(fib_memo, 2000, 10)
plt.plot(x, y)
#plt.plot(a, b)
plt.show()
