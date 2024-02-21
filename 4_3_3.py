import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from numpy import trapz

x = np.arange(0, 10)
y = np.abs(np.cos(x*np.exp(np.cos(x) + np.log(x+1))))
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()
ax.grid()
plt.plot(x, y)
plt.fill_between(x, y)
plt.show()
area = trapz(y)
print(area)