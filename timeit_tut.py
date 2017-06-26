import timeit


def costly_func(lst):
    return map(lambda x: x ** 2, lst)


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

sl = range(10)
ll = range(1000)
wrapped = wrapper(costly_func, sl)

print(timeit.timeit(wrapped, number=1000))

wrapped = wrapper(costly_func, ll)

print(timeit.timeit(wrapped, number=1000))
