from matplotlib import pyplot as plt 
import pandas as pd

with open('yakutsk_2019.csv') as f:
    print(f)

data = pd.read_csv('yakutsk_2019.csv', sep=';', encoding='cp1251')

T = data["Temp"]
print (T)
