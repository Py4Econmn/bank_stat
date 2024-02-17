import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('banks2312.xlsx')
df = df.T

df.columns = df.iloc[0,:]
df = df.iloc[1:,:]
df = df.rename(columns={'Индикатор нэр': 'Date'})
df.reset_index(drop=True,inplace=True)
df.columns = [col.strip() for col in df.columns]

df['Date'] = df['Date'].str.extract(r'(\d{4}-\d{2})')

df = df.rename(columns={'Төгрөгийн харилцах': 'ca_mnt','Гадаад валютын харилцах': 'ca_fx'})


df = df[['Date','ca_mnt','ca_fx','mnt_usd']]
df.columns= ['Date','ca_mnt','no','ca_fx','no','mnt_usd']
df = df[['Date','ca_mnt','ca_fx','mnt_usd']]
df['ca_fx_usd'] = df['ca_fx']/df['mnt_usd']
# df['ca_mnt_to_fx'] = df['ca_mnt']/df['ca_fx']
df['mnt_usd_000'] = df['mnt_usd']/1000
df['ca_mnt_000'] = df['ca_mnt']/1e6
df['ca_fx_usd_000'] = df['ca_fx_usd']/1e3*3
df['ca_fx_000'] = df['ca_fx']/1e6

df.plot(x='Date', y=['ca_mnt_000', 'ca_fx_000', 'mnt_usd_000','ca_fx_usd_000'], marker='o')
plt.show()

df.to_csv('hi.csv')


# df['d_ca_fx'] =  df['ca_fx_usd'].diff(2)/df['ca_fx_usd'].shift(2)
# df['d_mntusd'] =  df['mnt_usd'].diff().shift()/df['mnt_usd'].shift(2)
# # df['d1_ca_fx'] = df['d_ca_fx'].shift()

# df.plot.scatter(x='d_mntusd', y='d_ca_fx', title='CA in FX to MNT changes')
# plt.show()




