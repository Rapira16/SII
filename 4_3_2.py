import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = ((np.sqrt(1+np.exp(np.sqrt(x))+np.cos(np.square(x))))/(np.abs(1-np.power(np.sin(x), 3))))+np.log(np.abs(2*x))

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()
ax.grid()
plt.plot(x, y)
x=x[:5]
y=y[:5]
ax.scatter(x, y)
print(x)
plt.show()
