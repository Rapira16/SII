import numpy
import statistics
from matplotlib import pyplot

x = [i/10 for i in range(0, 10)]
rnd_arr = list(numpy.random.choice(x, 1000))
amount_data = []
for j in range(0, 10):
    amount_data.append(rnd_arr.count(x[j]))
print(amount_data)
print('среднее =', statistics.mean(rnd_arr))
print('медиана =', statistics.median(rnd_arr))
pyplot.show()
pyplot.grid()
pyplot.scatter(x, amount_data)
