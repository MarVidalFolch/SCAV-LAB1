# LAB 1 - EXERCISE 5: Create a script which can convert, can decode (or both) an input using the DCT. Not necessary a
# JPG encoder or decoder. A script only about DCT is OK too.

from skimage import io
import numpy as np
import math

# load the image and print its size
f = io.imread('output.png', as_gray=True)
print('image matrix size: ', f.shape)

pos: int = 175
size = 256
f = f[pos: pos + size, pos: pos + size]
print('image matrix: ', f)
# init some parameters
n = 8  # window in which we will perform the DCT
sumd = 0  # init value
r_ = []  # init value

# create some blank matrices to store our data:
dctmatrix = np.zeros(np.shape(f))  # create DCT matrix to plug values in
f = f.astype(np.int16)  # convert to be able to substract 128 from each pixel
f = f - 128
f2 = np.zeros(np.shape(f))  # matrix to store the compressed image


# define the cosine function that will be plugged into the DCT
def cosp(i, j, n):
    output = 0
    output = np.cos(((2 * i) + 1)) * j * math.pi / (2 * n)
    return output


# define the DCT function for nxn @ axb location
def DCT(f, n, u, v, a, b):
    sumd = 0
    for x in r_[0:n]:
        for y in r_[0:n]:
            u = u % n
            v = v % n
            sumd += f[x + a, y + b] * cosp(x, u, n) * cosp(y, v, n)
    if u == 0:
        sumd *= 1 / math.sqrt(2)
    else:
        sumd *= 1
    if v == 0:
        sumd *= 1 / math.sqrt(2)
    else:
        sumd *= 1
    sumd *= 1 / math.sqrt(2 * n)

    return sumd


print(sumd)
# run the DCT across the entire image in nxn intervals
for a in r_[0:np.shape(f)[0]:n]:
    for b in r_[0:np.shape(f)[1]:n]:
        for u in r_[a:a + n]:
            for v in r_[b:b + n]:
                dctmatrix[u, v] = DCT(f, n, u, v, a, b)
