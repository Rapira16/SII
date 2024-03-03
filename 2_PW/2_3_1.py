import pandas as pd
x = pd.Series([1, 3, 5, 2])
y = pd.Series([4, 2, 3, 8])
print(((x-y)**2)**0.5)
