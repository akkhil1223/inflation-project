import pandas as pd
import os
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:/Users/akhar/OneDrive/Desktop/inflation_project/inflate.csv' , encoding = 'latin1')
df.dropna(inplace = True)
print(df.head(10))
x = df['Inflation'].mean()
print("mean inflation in asia is",x)

