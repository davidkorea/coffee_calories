# coffee_calories
 
# 1. pandas

**an upgrade package from numpy and matplotlib.pyplot**

1. read file - dataframe
```php
data_df = pd.read_csv('./Beijing_PM.csv')
```
  - ```print('head(): {}'.format(data_df.head(10)))```
    ```
     head():    year  month  day  hour  season  PM_China  PM_US
     0  2013      1    1     0       4       NaN   31.0
     1  2013      1    1     1       4       NaN   32.0
     2  2013      1    1     2       4       NaN   21.0
     3  2013      1    1     3       4       NaN   16.0
     4  2013      1    1     4       4       NaN   15.0
     5  2013      1    1     5       4       NaN    9.0
     6  2013      1    1     6       4       NaN    9.0
     7  2013      1    1     7       4       NaN    7.0
     8  2013      1    1     8       4       NaN   14.0
     9  2013      1    1     9       4       NaN   11.0
    ```
  - ```print('describe(): {}'.format(data_df.describe()))```
    ```
    describe():                year         month           day          hour        season  \
    count  26280.000000  26280.000000  26280.000000  26280.000000  26280.000000
    mean    2014.000000      6.526027     15.720548     11.500000      2.490411
    std        0.816512      3.447917      8.796414      6.922318      1.116788
    min     2013.000000      1.000000      1.000000      0.000000      1.000000
    25%     2013.000000      4.000000      8.000000      5.750000      1.000000
    50%     2014.000000      7.000000     16.000000     11.500000      2.000000
    75%     2015.000000     10.000000     23.000000     17.250000      3.000000
    max     2015.000000     12.000000     31.000000     23.000000      4.000000
                PM_China         PM_US
    count  20508.000000  25970.000000
    mean      92.560806     94.094686
    std       88.027434     93.806554
    min        3.000000      1.000000
    25%       28.000000     27.000000
    50%       68.000000     66.000000
    75%      127.000000    126.000000
    max      672.000000    886.000000
    ```
  - ```print('info(): {}'.format(data_df.info()))```
    ```
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 26280 entries, 0 to 26279
    Data columns (total 7 columns):
    year        26280 non-null int64
    month       26280 non-null int64
    day         26280 non-null int64
    hour        26280 non-null int64
    season      26280 non-null int64
    PM_China    20508 non-null float64
    PM_US       25970 non-null float64
    dtypes: float64(2), int64(5)
    memory usage: 1.4 MB
    info(): None
    ```
2. groupby
```php
groupby_year = data_df.groupby('year')
# An other data type that will return all columns of origin data
```
3. calculate
```php
pm_china_mean = groupby_year['PM_China'].mean()
pm_us_mean = groupby_year['PM_US'].mean()
```
