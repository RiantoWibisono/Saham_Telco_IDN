# ========================================================================================================
# Harga Historis Saham Provider Telco Indonesia (April 2019)
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
    df1['2019-04'].index, df1['2019-04']['Close'], 'g',
    df2['2019-04'].index, df2['2019-04']['Close'], 'c',
    df3['2019-04'].index, df3['2019-04']['Close'], 'b',
    df4['2019-04'].index, df4['2019-04']['Close'], 'r'
)

plt.title('Harga Historis Saham Provider Telco Indonesia', fontsize = 15, fontweight="bold")
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.grid(True)
plt.legend(['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk'], loc= 'upper center', ncol = 4, fontsize = 7)
plt.xticks(df1['2019-04'].index[::1], rotation = 60)

plt.subplots_adjust(bottom=.2)

plt.show()