import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
def get_chinese_font():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

def df_info(data_df):
    print('head(): {}'.format(data_df.head(10)))
    print('describe(): {}'.format(data_df.describe()))
    print('info(): {}'.format(data_df.info()))

def group_bar(pm_china_mean,pm_us_mean):
    bar_locs = np.arange(3)
    bar_width = 0.35    
    
    xticks_labels = ['2013','2014','2015']
    
    plt.figure()
    plt.bar(bar_locs, pm_china_mean, width=bar_width, color='b', alpha=0.7, label='中国')
    plt.bar(bar_locs + bar_width, pm_us_mean, width=bar_width, color='g', alpha=0.7, label='美国')
    # plt.bar() 前两个参数顺序不能变
    
    plt.xticks(bar_locs + bar_width / 2, xticks_labels, fontproperties=get_chinese_font())
    plt.ylabel('PM2.5 平均值', fontproperties=get_chinese_font())
    plt.title('中国vs美国测量值对比图', fontproperties=get_chinese_font())
    plt.legend(loc='best', prop=get_chinese_font())
    
    plt.tight_layout()
    plt.savefig('./group_bar.png')
    plt.show()

def main():
    data_df = pd.read_csv('./Beijing_PM.csv')
    df_info(data_df)
    groupby_year = data_df.groupby('year')
    pm_china_mean = groupby_year['PM_China'].mean()
    pm_us_mean = groupby_year['PM_US'].mean()
    pm_china_mean.plot(kind='bar')

    group_bar(pm_china_mean, pm_us_mean)

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