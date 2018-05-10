import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_df = pd.read_csv('./Beijing_PM.csv')
data_df.dropna(inplace=True)

#1 2013-2015 CN vs US
grouped_year_df = data_df.groupby('year')[ ['PM_China','PM_US'] ].mean()
grouped_year_df.plot(kind='bar',rot=0,title='2013-2015 CN vs US')
plt.tight_layout()
# plt.show()

#2 rank = [excellent,good,bad] stacked bar
data_df['Level_cn'] = pd.cut(data_df['PM_China'],
                             bins=[-np.inf,50,100,500,np.inf],
                             labels=['Excellent','Good','Bad','Die'])
data_df['Level_us'] = pd.cut(data_df['PM_US'],
                             bins=[-np.inf,50,100,500,np.inf],
                             labels=['Excellent','Good','Bad','Die'])
# pivot_df = pd.pivot_table(data_df,index='year',columns=['Level_cn','Level_us'],
#                           values=['day'],aggfunc='count')
# columns - outer level -> inner level
# values - different pivor due to diffenent value
pivot_cn = pd.pivot_table(data_df,index='year',columns=['Level_cn'],
                          values=['day'],aggfunc='count')
pivot_cn['day'].plot(kind='bar',stacked=True,rot=0)
# plt.show()

pivot_us = pd.pivot_table(data_df,index='year',columns=['Level_us'],
                       values=['day'],aggfunc='count')
pivot_us['day'].plot(kind='bar',stacked=True,rot=0)
# plt.show()

#3 Resample freq=1h -> 1day
# data_df['year'] = pd.to_datetime(data_df['year'])
data_df['hour'] = data_df['hour'].astype('str') + ':00'
# data_df.set_index(data_df['year'])
# data_df['day_mean_cn'] = data_df.resample('D').mean()
print()