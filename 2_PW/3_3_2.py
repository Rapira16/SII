from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

data = pd.read_csv('https://raw.githubusercontent.com/akmand/datasets/master/iris.csv')
data['sepal_length_cm'] = MinMaxScaler().fit_transform(np.array
 (data['sepal_length_cm']).reshape(-1, 1))
display(data)
data['sepal_width_cm'] = (data['sepal_width_cm'] - data['sepal_width_cm'].mean())
/ data['sepal_width_cm'].std()
display(data)