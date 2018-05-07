import pandas as pd
import matplotlib.pyplot as plt
import os

def df_info(data_df):
    print('head(): {}'.format(data_df.head(10)))
    print('describe(): {}'.format(data_df.describe()))
    print('info(): {}'.format(data_df.info()))


def main():
    data_df = pd.read_csv('./Beijing_PM.csv')
    df_info(data_df)
    groupby_year = data_df.groupby('year')
    pm_china_mean = groupby_year['PM_China'].mean()
    pm_us_mean = groupby_year['PM_US'].mean()
    pm_china_mean.plot(kind='bar')

    pm_china_mean.to_csv('./pm_china_mean.csv')
    pm_us_mean.to_csv('./pm_us_mean.csv')

    plt.title('PM 2.5 - China')
    plt.tight_layout()
    plt.savefig('./pm_china_mean.png')
    plt.show()
    pm_us_mean.plot(kind='bar')
    plt.title('PM 2.5 - US')
    plt.tight_layout()
    plt.savefig('./pm_us_mean.png')
    plt.show()



main()