import sys
sys.path.append('/Users/billma/anaconda/lib/python3.6/site-packages')

from scipy.misc import imread, imsave, imresize
import numpy as np
import matplotlib.pyplot as plt

img = imread('cat.jpg')
print(img.dtype, img.shape)

img_tinted = img * [1,0.95,0.9]

plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)

plt.imshow(np.uint8(img_tinted))
plt.show()
