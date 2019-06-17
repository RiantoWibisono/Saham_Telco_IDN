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
# dftanggal = pd.read_csv(
#     './saham/TLKM.JK.csv', 
#     index_col = False
# )
# tanggal = []
# for i in dftanggal['Date']:
#     tanggal.append(str(i))
# # a = np.array(tanggal)

df1 = df1.set_index('Date') 
df2 = df2.set_index('Date') 
df3 = df3.set_index('Date') 
df4 = df4.set_index('Date') 

# plt.style.use('seaborn')
plt.plot(
    df1.index, df1['Close'], 'g',
    df2.index, df2['Close'], 'c',
    df3.index, df3['Close'], 'b',
    df4.index, df4['Close'], 'r'
)


plt.title('Harga Historis Saham Provider Telco Indonesia', fontsize = 15, fontweight="bold")
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.grid(True)
plt.legend(['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk'], loc= 'upper center', ncol = 4, fontsize = 7)
# plt.xticks(np.arange(min((df1.index)), max(df1.index)+1, 7.0))

plt.subplots_adjust(bottom=.2)

plt.show()