import numpy as np
import time
start = time.time()
x = np.ones([1000, 1000])
x[::2, ::2] = 0
x[1::2, 1::2] = 0
print(x, time.time() - start)