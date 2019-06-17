import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

dftanggal = pd.read_csv(
    './saham/TLKM.JK.csv', 
    index_col = False
)
tanggal = []
for i in dftanggal['Date']:
    tanggal.append(str(i))
# print(tanggal)

a = pd.Series(tanggal)
print(a[::5])

