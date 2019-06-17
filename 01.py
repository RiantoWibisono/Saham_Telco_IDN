# ========================================================================================================
# Harga Historis Saham Provider Telco Indonesia 
# ========================================================================================================
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df1 = pd.read_csv(
    './saham/EXCL.JK.csv', 
    index_col = False,
    parse_dates=['Date']
)

df2 = pd.read_csv(
    './saham/FREN.JK.csv', 
    index_col = False,
    parse_dates=['Date']
)
df3 = pd.read_csv(
    './saham/ISAT.JK.csv', 
    index_col = False,
    parse_dates=['Date']
)
df4 = pd.read_csv(
    './saham/TLKM.JK.csv', 
    index_col = False,
    parse_dates=['Date']
)

df1 = df1.set_index('Date') 
df2 = df2.set_index('Date') 
df3 = df3.set_index('Date') 
df4 = df4.set_index('Date') 

plt.style.use('seaborn')
plt.plot(
    df1.index, df1['Close'], 'g',
    df2.index, df2['Close'], 'c',
    df3.index, df3['Close'], 'b',
    df4.index, df4['Close'], 'r'
)

plt.suptitle('Harga Historis Saham Provider Telco Indonesia', fontsize = 15, fontweight="bold")
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.grid(True)
label = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(label, loc = 'upper center', bbox_to_anchor = (0.5, 1.08), ncol = 4, frameon = False, fontsize = 8)
plt.xticks(rotation = 60)

plt.subplots_adjust(bottom=.2)

plt.show()