import pandas as pd
import matplotlib.pyplot as plt

file = 'study/machineLearning/library/boston_housing.csv'
boston_df = pd.read_csv(file).drop('CAT. MEDV', axis=1)
# print(boston_df.head(), boston_df.shape)
# print(boston_df.info())
print(boston_df.describe())

