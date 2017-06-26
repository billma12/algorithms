def fibbonaci(n):
    # recursive
    if n < 2:
        return 1
    return fibbonaci(n - 2) + fibbonaci(n - 1)


def fibbonaci2(n):
    # iterative
    a, b = 1, 1
    for i in range(n - 1):
        c = a + b
        b = a
        a = c

    return c


def fibbonaci3(n, lookup):
    # memoization
    if n < 2:
        return 1
    if n in lookup:
        return lookup[n]
    else:
        lookup[n] = fibbonaci3(n - 2, lookup) + fibbonaci3(n - 1, lookup)

    return lookup[n]

n = 35
print(fibbonaci(n))
print(fibbonaci2(n))
lookup = {}
print(fibbonaci3(n, lookup))
