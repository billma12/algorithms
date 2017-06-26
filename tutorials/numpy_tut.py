import sys
sys.path.append('/Users/billma/anaconda/lib/python3.6/site-packages')
import numpy as np

a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])

a = np.zeros((2, 2))
print(a)

e = np.random.random((2, 2))
print(e)
