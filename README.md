# coffee_calories
 
# 1. pandas

**an upgrade package from numpy and matplotlib.pyplot**

1. read file - dataframe
```php
data_df = pd.read_csv('./Beijing_PM.csv')
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
