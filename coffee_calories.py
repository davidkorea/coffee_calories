import pandas as pd
import os
import matplotlib.pyplot as plt

DATA_FILE = './data_pd/coffee_menu.csv'
# print(os.path.exists(DATA_FILE))

def main():
    data_df = pd.read_csv(DATA_FILE)
    cate_groupby = data_df.groupby('Beverage_category')
    cate_count = cate_groupby['Calories'].count()
    cal_mean = cate_groupby['Calories'].mean()
    print(cate_count, cal_mean)
    cate_count.plot(kind='bar')
    plt.title('Category count')
    plt.tight_layout()
    plt.show()
    cal_mean.plot(kind='bar')
    plt.title('Mean calories')
    plt.tight_layout()
    plt.show()

main()