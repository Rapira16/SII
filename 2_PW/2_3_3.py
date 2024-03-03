import pandas as pd

data = pd.read_csv("adult.csv")
print(data.head(4))  # первые 4 строки
print(data.tail(3))  # последние 3 строки
print(data.shape)  # размер таблицы
print(data.describe())  # данные о таблице
print(data.iloc[101:114])  # все строки в промежутке
print(data[data['age'] <= 20].tail(5))  # последние пять, у которых возраст меньше 20
