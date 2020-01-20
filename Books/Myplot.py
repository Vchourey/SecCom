import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import urllib

# https://www.nseindia.com/products/content/sec_bhavdata_full.csv
# data:application/csv;charset=utf-8,%22Symbol%22%2C%22Series%22%2C%22Date%22%2C%22Prev%20Close%22%2C%22Open%20Price%22%2C%22High%20Price%22%2C%22Low%20Price%22%2C%22Last%20Price%22%2C%22Close%20Price%22%2C%22Average%20Price%22%2C%22Total%20Traded%20Quantity%22%2C%22Turnover%22%2C%22No.%20of%20Trades%22%2C%22Deliverable%20Qty%22%2C%22%25%20Dly%20Qt%20to%20Traded%20Qty%22%0A%22TATASTEEL%22%2C%22EQ%22%2C%2206-Feb-2019%22%2C%22%20%20%20%20%20%20%20%20464.70%22%2C%22%20%20%20%20%20%20%20%20466.00%22%2C%22%20%20%20%20%20%20%20%20486.70%22%2C%22%20%20%20%20%20%20%20%20463.80%22%2C%22%20%20%20%20%20%20%20%20484.85%22%2C%22%20%20%20%20%20%20%20%20485.10%22%2C%22%20%20%20%20%20%20%20%20477.98%22%2C%22%20%20%2010999265%22%2C%22%20%20%20%20%20%20%20%20%20%205257387351.25%22%2C%22%20%20%20%20%20165202%22%2C%22%20%20%20%203590380%22%2C%22%20%20%20%20%20%20%20%20%2032.64%22%0A%22TATASTEEL%22%2C%22EQ%22%2C%2207-Feb-2019%22%2C%22%20%20%20%20%20%20%20%20485.10%22%2C%22%20%20%20%20%20%20%20%20483.45%22%2C%22%20%20%20%20%20%20%20%20491.40%22%2C%22%20%20%20%20%20%20%20%20478.10%22%2C%22%20%20%20%20%20%20%20%20488.20%22%2C%22%20%20%20%20%20%20%20%20489.05%22%2C%22%20%20%20%20%20%20%20%20486.31%22%2C%22%20%20%20%207857338%22%2C%22%20%20%20%20%20%20%20%20%20%203821106588.00%22%2C%22%20%20%20%20%20103008%22%2C%22%20%20%20%201791138%22%2C%22%20%20%20%20%20%20%20%20%2022.80%22%0A%22TATASTEEL%22%2C%22EQ%22%2C%2208-Feb-2019%22%2C%22%20%20%20%20%20%20%20%20489.05%22%2C%22%20%20%20%20%20%20%20%20483.00%22%2C%22%20%20%20%20%20%20%20%20487.75%22%2C%22%20%20%20%20%20%20%20%20465.95%22%2C%22%20%20%20%20%20%20%20%20468.70%22%2C%22%20%20%20%20%20%20%20%20468.75%22%2C%22%20%20%20%20%20%20%20%20477.99%22%2C%22%20%20%20%208414514%22%2C%22%20%20%20%20%20%20%20%20%20%204022025585.45%22%2C%22%20%20%20%20%20%2093170%22%2C%22%20%20%20%201992658%22%2C%22%20%20%20%20%20%20%20%20%2023.68%22%0A%22TATASTEEL%22%2C%22EQ%22%2C%2211-Feb-2019%22%2C%22%20%20%20%20%20%20%20%20468.75%22%2C%22%20%20%20%20%20%20%20%20475.00%22%2C%22%20%20%20%20%20%20%20%20487.00%22%2C%22%20%20%20%20%20%20%20%20460.30%22%2C%22%20%20%20%20%20%20%20%20479.75%22%2C%22%20%20%20%20%20%20%20%20480.70%22%2C%22%20%20%20%20%20%20%20%20475.08%22%2C%22%20%20%2023262314%22%2C%22%20%20%20%20%20%20%20%20%2011051425898.10%22%2C%22%20%20%20%20%20235446%22%2C%22%20%20%20%201799162%22%2C%22%20%20%20%20%20%20%20%20%20%207.73%22%0A%22TATASTEEL%22%2C%22EQ%22%2C%2212-Feb-2019%22%2C%22%20%20%20%20%20%20%20%20480.70%22%2C%22%20%20%20%20%20%20%20%20478.40%22%2C%22%20%20%20%20%20%20%20%20497.20%22%2C%22%20%20%20%20%20%20%20%20476.70%22%2C%22%20%20%20%20%20%20%20%20486.55%22%2C%22%20%20%20%20%20%20%20%20487.40%22%2C%22%20%20%20%20%20%20%20%20489.80%22%2C%22%20%20%2018836111%22%2C%22%20%20%20%20%20%20%20%20%20%209225953102.25%22%2C%22%20%20%20%20%20201556%22%2C%22%20%20%20%202898188%22%2C%22%20%20%20%20%20%20%20%20%2015.39%22%0A
d = [1, 2, 3, 4, 5, 6, 7, 8]
x = [32, 34, 45, 43, 52, 36, 37, 48]
y = [35, 38, 49, 47, 62, 46, 47, 58]
z = [42, 38, 49, 63, 72, 56, 57, 68]
# plt.plot(d, x, color='green', marker='D', linestyle='--', markersize=10, alpha=0.5, label="MIN")
# plt.plot(d, y, color='green', marker='D', linestyle='--', markersize=10, alpha=0.5, label="AVG")
# plt.plot(d, z, color='green', marker='D', linestyle='--', markersize=10, alpha=0.5, label="MAX")
# plt.bar(d, x, color='green', label="MIN")
# plt.scatter(d, x, color='green', marker='D', s=100, alpha=0.5, label="MIN")
# plt.stackplot(d,x,y,z, colors=['m', 'k', 'R', 'c'])
''' 
activity = ['sleep', 'deep', 'walk', 'running', 'play', 'eating', 'reading', 'gaming']
plt.pie(d,
        labels=activity,
        colors=['m', 'k', 'R', 'c', 'm', 'k', 'R', 'c'],
        shadow=True,
        startangle=90,
        explode=(0, 0.1, 0, 0, 0, 0.1, 0, 0),
        autopct='%1.1f%%')
'''
''''
# loading data form file
import csv
x = []
y = []
with open("testdata.xlsx", 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[0]))
        y.append((row[3]))

plt.plot(x, y)
'''
''''
def tatasteel(stock):

    stock_url = 'data:application/csv;charset=utf-8,%22Symbol%22%2C%22Series%22%2C%22Date%22%2C%22Prev%20Close%22%2C%22Open%20Price%22%2C%22High%20Price%22%2C%22Low%20Price%22%2C%22Last%20Price%22%2C%22Close%20Price%22%2C%22Average%20Price%22%2C%22Total%20Traded%20Quantity%22%2C%22Turnover%22%2C%22No.%20of%20Trades%22%2C%22Deliverable%20Qty%22%2C%22%25%20Dly%20Qt%20to%20Traded%20Qty%22%0A%22TATASTEEL%22%2C%22EQ%22%2C%2206-Feb-2019%22%2C%22%20%20%20%20%20%20%20%20464.70%22%2C%22%20%20%20%20%20%20%20%20466.00%22%2C%22%20%20%20%20%20%20%20%20486.70%22%2C%22%20%20%20%20%20%20%20%20463.80%22%2C%22%20%20%20%20%20%20%20%20484.85%22%2C%22%20%20%20%20%20%20%20%20485.10%22%2C%22%20%20%20%20%20%20%20%20477.98%22%2C%22%20%20%2010999265%22%2C%22%20%20%20%20%20%20%20%20%20%205257387351.25%22%2C%22%20%20%20%20%20165202%22%2C%22%20%20%20%203590380%22%2C%22%20%20%20%20%20%20%20%20%2032.64%22%0A%22TATASTEEL%22%2C%22EQ%22%2C%2207-Feb-2019%22%2C%22%20%20%20%20%20%20%20%20485.10%22%2C%22%20%20%20%20%20%20%20%20483.45%22%2C%22%20%20%20%20%20%20%20%20491.40%22%2C%22%20%20%20%20%20%20%20%20478.10%22%2C%22%20%20%20%20%20%20%20%20488.20%22%2C%22%20%20%20%20%20%20%20%20489.05%22%2C%22%20%20%20%20%20%20%20%20486.31%22%2C%22%20%20%20%207857338%22%2C%22%20%20%20%20%20%20%20%20%20%203821106588.00%22%2C%22%20%20%20%20%20103008%22%2C%22%20%20%20%201791138%22%2C%22%20%20%20%20%20%20%20%20%2022.80%22%0A%22TATASTEEL%22%2C%22EQ%22%2C%2208-Feb-2019%22%2C%22%20%20%20%20%20%20%20%20489.05%22%2C%22%20%20%20%20%20%20%20%20483.00%22%2C%22%20%20%20%20%20%20%20%20487.75%22%2C%22%20%20%20%20%20%20%20%20465.95%22%2C%22%20%20%20%20%20%20%20%20468.70%22%2C%22%20%20%20%20%20%20%20%20468.75%22%2C%22%20%20%20%20%20%20%20%20477.99%22%2C%22%20%20%20%208414514%22%2C%22%20%20%20%20%20%20%20%20%20%204022025585.45%22%2C%22%20%20%20%20%20%2093170%22%2C%22%20%20%20%201992658%22%2C%22%20%20%20%20%20%20%20%20%2023.68%22%0A%22TATASTEEL%22%2C%22EQ%22%2C%2211-Feb-2019%22%2C%22%20%20%20%20%20%20%20%20468.75%22%2C%22%20%20%20%20%20%20%20%20475.00%22%2C%22%20%20%20%20%20%20%20%20487.00%22%2C%22%20%20%20%20%20%20%20%20460.30%22%2C%22%20%20%20%20%20%20%20%20479.75%22%2C%22%20%20%20%20%20%20%20%20480.70%22%2C%22%20%20%20%20%20%20%20%20475.08%22%2C%22%20%20%2023262314%22%2C%22%20%20%20%20%20%20%20%20%2011051425898.10%22%2C%22%20%20%20%20%20235446%22%2C%22%20%20%20%201799162%22%2C%22%20%20%20%20%20%20%20%20%20%207.73%22%0A%22TATASTEEL%22%2C%22EQ%22%2C%2212-Feb-2019%22%2C%22%20%20%20%20%20%20%20%20480.70%22%2C%22%20%20%20%20%20%20%20%20478.40%22%2C%22%20%20%20%20%20%20%20%20497.20%22%2C%22%20%20%20%20%20%20%20%20476.70%22%2C%22%20%20%20%20%20%20%20%20486.55%22%2C%22%20%20%20%20%20%20%20%20487.40%22%2C%22%20%20%20%20%20%20%20%20489.80%22%2C%22%20%20%2018836111%22%2C%22%20%20%20%20%20%20%20%20%20%209225953102.25%22%2C%22%20%20%20%20%20201556%22%2C%22%20%20%20%202898188%22%2C%22%20%20%20%20%20%20%20%20%2015.39%22%0A'
    source = urllib.request.urlopen(stock_url).read().decode()
    Symbol, Series, Date, Prev, Close, Open, Price, High, Price, Low, Price, Last, Price, Close, Price, Average, Price, Total, Traded, Quantity, Turnover = np.loadtxt('TATACOFFEEEQN,CSV', delimiter=',', unpack=True)
    plt.plot(Date, Open)
    plt.title('temperature polt')
    plt.xlabel("day's")
    plt.ylabel('temperature')
    plt.legend(loc="best",shadow=True, fontsize='small')
    plt.grid()
    plt.show()
tatasteel(1)
'''
import pandas as pd
# data = {'a': 0., 'b': 1., 'c': 2.}
# s = pd.Series([2,2,5,4],index=['b','c','d','a'])
# print(s['a'])
'''
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d, dtype=float)
df['three']=pd.Series([10,20,30],index=['a','b','c'])
df['four']=df['one']+df['three']
del df['two']
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.drop(df2)

print(df)


df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])


for value in df2.itertuples():
   print(value)

'''

# Sorting - index
'''
unsorted_df = pd.DataFrame(np.random.randn(10, 2), index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
sorted_df = unsorted_df.sort_index(axis=0, ascending=False)
print(sorted_df)

# Sorting - values
unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4],}, index=[1,4,2,3])
sorted_df = unsorted_df.sort_values(by=['col1', 'col2'], ascending=False, kind='quicksort')
print(sorted_df)
'''

''''
# option customization
pd.set_option("display.max_rows", 120)
print(pd.get_option("display.max_rows"))
pd.reset_option("display.max_columns", 120)
print(pd.get_option("display.max_columns"))
print(pd.describe_option("display.max_rows"))
'''

'''
# indexing and selecting data
df = pd.DataFrame(np.random.randn(8, 4), index=['a','b','c','d','e','f','g','h'], columns=['A', 'B', 'C', 'D'])
print(df[['A', 'B']])
print(df.loc[:, ['A', 'C']])
print(df.iloc[1:5, 2:4])
print(df.ix[['a', 'b', 'c'], 1:3])
'''
'''
#Statistical Functions

s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
# print(s1.pct_change()*100)
df = pd.DataFrame(np.random.randn(8, 4), index=['a','b','c','d','e','f','g','h'], columns=['A', 'B', 'C', 'D'])
print(df)
# print(df.pct_change(axis=1)*100)
#print(s1.cov(s2))
#print(df['A'].cov(df['B']))
#print(df['A'].corr(df['D']))
df['B']=df['D']
print(df.rank(method='first'))
'''

'''
# Window Functions
df = pd.DataFrame(np.random.randn(10, 4),
      index=pd.date_range('1/1/2019', periods=10),
      columns=['A', 'B', 'C', 'D'])
print(df)
# print(df.rolling(window=3).max())
# print(df.expanding(min_periods=3).min())
#print(df.ewm(com=0.5).mean())

# Aggregations
S = df.rolling(window=3, min_periods=1)
print(S.aggregate(np.sum))
print(S['A', 'C'].aggregate(np.sum))
print(S['A', 'B'].aggregate([np.sum, np.mean, np.max]))
print(S.aggregate({'A': np.sum, 'B': np.mean, 'C': np.max}))
'''
'''
#Missing Data

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
print(df)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
print(df.isnull())
print(df['one'].notnull())
print(df.fillna(method='bfill'))
print(df.dropna(axis=1))
df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]},index=['a', 'c', 'e', 'f', 'h', 'b'])
print(df.replace({1000:10, 0:20}))
'''
'''
# GroupBy( Splitting the Object, Applying a function,  Combining the results)
# Aggregation
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)
print(df.groupby('Team'))
print(df.groupby(['Team', 'Year']).groups)
grouped = df.groupby('Year')
print(grouped.get_group(2014))
print(grouped['Points'].agg(np.mean))
print(grouped['Points'].aggregate([np.mean, np.sum, np.size]))
score = lambda x: (x - x.mean()) / x.std()*10
print(grouped['Rank' ].transform(score))
print(df.groupby('Team').filter(lambda x: len(x)>=3))
for name, group in grouped:
   print(name)
   print(group)
'''
'''
# Merging/Joining
dfl = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
dfr = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id': ['sub2','sub4','sub3','sub6','sub5']})

print(pd.merge(dfl, dfr, on='id'))
print(pd.merge(dfl, dfr, on=['id', 'subject_id']))
print(pd.merge(dfl, dfr, on='subject_id', how='left'))
print(pd.merge(dfl, dfr, on='subject_id', how='right'))
print(pd.merge(dfl, dfr, on='subject_id', how='inner'))
print(pd.merge(dfl, dfr, on='subject_id', how='outer'))
'''

'''
# concatenation

dfone = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

dftwo = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])

print(pd.concat([dfone, dftwo], keys=['X', 'Y']))
print(pd.concat([dfone, dftwo], keys=['X', 'Y'], ignore_index='True'))
print(pd.concat([dfone, dftwo], axis=1))
print(dfone.append([dftwo, dfone, dftwo], ignore_index='True'))
'''

'''
# Time Series
print(pd.datetime.now())
print(pd.Timestamp('2017-03-01'))
print(pd.Timestamp(1587687255,unit='s'))
print(pd.date_range("11:00", "13:30", freq="30min").time)
print(pd.date_range("11:00", "13:30", freq="H").time)
print(pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None])))
print(pd.to_datetime(['2005/11/23', '2010.12.31', None]))

# Date Functionality
print(pd.date_range('1/1/2018', periods=10))
print(pd.date_range('1/1/2018', periods=10, freq='BMS'))
print(pd.bdate_range('1/1/2019', periods=10,))
start = pd.datetime(2011, 1, 1)
end = pd.datetime(2011, 1, 5)
print(pd.date_range(start, end))
print(pd.date_range(start='1/1/2019', end='1/10/2019'))
'''
'''
# Timedelta
print(pd.Timedelta('2 days 2 hours 15 minutes 30 seconds')) # with string
print(pd.Timedelta(10, unit='h'))
print(pd.Timedelta(days=2))
print(pd.to_timedelta(5))
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([pd.Timedelta(days=i) for i in range(3)])
df = pd.DataFrame(dict(A=s, B=td))
print(df)
df['C'] = df['A']+df['B']
print(df)
df['D'] = df['C']-df['B']
print(df)
'''
'''
# Categorical

s = pd.Series(["a","b","c","a"], dtype="category")
print(s)
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print(cat)
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print(cat)
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print(cat)
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", "a", "c", "c", np.nan]})
print(df.describe())
s = s.cat.add_categories([4])
print(s.cat.categories)
print(s.cat.remove_categories("a"))

cat0 = pd.Series([1,2,3]).astype("category", categories=[1,2,3], ordered=True)
cat1 = pd.Series([2,2,2]).astype("category", categories=[1,2,3], ordered=True)

print(cat0>cat1)
'''
'''
# Visualization

df = pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))
print(df.plot())
print(df.plot.bar())
print(df.plot.barh(stacked=True))
print(df.plot.barh(stacked=True))
df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':np.random.randn(1000) - 1},
                columns=['a', 'b', 'c'])
print(df.plot.hist(bins=20))
# print(df.diff.hist(bins=20))

df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
print(df.plot.box())
print(df.plot.area())
print(df.plot.scatter(x='A', y='B'))

df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df1 = df.plot.pie(subplots=True)
print(df1)
'''
'''
# IO Tools
#pandas.read_csv(filepath_or_buffer, sep='\t', delimiter=None, header='infer',
#                names=None, index_col=None, usecols=None)
df=pd.read_csv("demodata.csv")          # read csv file
print(df)
df=pd.read_csv("demodata.csv",index_col=['clientid'])   # custom index
print(df)
df = pd.read_csv("demodata.csv", dtype={'prices': np.float64})  # Converters
df=pd.read_csv("demodata.csv", names=['a', 'b', 'c','d','e'])    # header_names
print(df)
df=pd.read_csv("demodata.csv",names=['a','b','c','d','e'],header=0)     #header
print(df)
df=pd.read_csv("demodata.csv", skiprows=5)                          # skiprows
print(df)
'''

'''
# Sparse Data / compressed
ts = pd.Series(np.random.randn(10))
ts[2:-4] = np.nan
print(ts.to_sparse())
df = pd.DataFrame(np.random.randn(10000, 4))
df.ix[:9998] = np.nan
ds = df.to_sparse()
print(ds.density)
print(ds.to_dense())
'''
'''
# Caveats & Gotchas

if pd.Series([False, True, False]).any():
    print('is it true')
print(pd.Series([ False]).bool())
s = pd.Series(range(5))
print(s==3)
print(s>=2)
print(s.isin([1, 3]))
# Reindexing vs ix Gotcha
df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three', 'four'], index=list('abcdef'))
print(df)
print(df.ix[['b', 'c', 'e']])
print(df.reindex(['b', 'c', 'e']))
print(df.ix[[1, 3, 5]])
print(df.reindex([1, 3, 5]))
'''

# NumPy Tutorial
'''
# Ndarray Object [numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)]

a = np.array([1, 2, 3])
print(a)
a = np.array([[1, 2], [3, 4]])
print(a)
a = np.array([1, 2, 3, 4, 5], ndmin=2, dtype=complex)
print(a)

# Data Types
print(np.dtype(np.int32))
print(np.dtype('i4'))   # int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc.
print(np.dtype('>i4'))
dt = np.dtype([('age', np.int8)])
print(dt)
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)
print(a['age'])

student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype=student)
print(a, a['name'], a['age'], a['marks'])
'''

#  Attributes
'''
# ndarray.shape/reshape
a = np.array([[1,2,3],[4,5,6]])
print(a, a.shape)
a.shape = (3,2)
print(a, a.shape)
print(a.reshape(2, 3))

# ndarray.ndim
a = np.arange(24)
print(a, ',', a.ndim)
b = a.reshape(2, 4, 3)
print(b, ',', b.shape, ',', b.ndim)

# numpy.itemsize
print(a.itemsize, ',', b.itemsize)
'''

# Array Creation Routines

'''
# numpy.empty (shape, dtype = float, order = 'C')
x = np.empty([3, 2], dtype=int)
print(x)
# numpy.zeros(shape, dtype = float, order = 'C')
x = np.zeros((5, 2), dtype=np.int)
print(x)
# numpy.ones(shape, dtype = None, order = 'C')
x = np.ones([2, 2], dtype=int)
print(x)
'''

# Array From Existing Data
'''
# numpy.asarray
x = [1, 2, 3]
a = np.asarray(x)
print(a)
y = (1, 2, 3)
a = np.asarray(y, dtype=float)
print(a)
z = [(1, 2, 3), (4, 5)]
a = np.asarray(z)
print(a)
# numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
s = 'Hello World'
#a = np.frombuffer(s, dtype='S1')
print(a)
# numpy.fromiter(iterable, dtype, count = -1)
list = range(5)
it = iter(list)
x = np.fromiter(it, dtype=float)
print(x)
'''

# Array From Numerical Ranges
'''
# numpy.arange(start, stop, step, dtype)
print(np.arange(5, dtype=float))
print(np.arange(10, 20, 2))
# numpy.linspace(start, stop, num, endpoint, retstep, dtype)
print(np.linspace(10, 20, 5))
print(np.linspace(10, 20, 5, endpoint=False, retstep=True))
print(np.linspace(1, 2, 5, retstep=True))
# numpy.logspace(start, stop, num, endpoint, base, dtype)
print(np.logspace(1, 2, num=10))
print(np.logspace(1, 10, num=10, base=2))
'''

'''
# Indexing & Slicing
a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])
print(a[2:6:2])
print(a[5], a[2:], a[2:5])

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)
print(a[..., 1:])

# Advanced Indexing
#Integer Indexing
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 1]]
print(y)
z = x[[0, 2, 1], [0, 1, 0]]
print(z)

x = np.array([[0,  1,  2], [3,  4,  5], [6,  7,  8], [9, 10, 11]])
print(x)
rows = np.array([[0,0], [3,3], [1, 1]])
cols = np.array([[0,2], [0,2], [0, 2]])
y = x[rows, cols]
print(y)
z = x[1:4, 1:3]     # slicing
y = x[1:4, [1, 2]]    # advanced index
# Boolean Array Indexing
print(x[x > 5])
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])
a = np.array([1, 2+6j, 5, 3.5+5j])
print(a[np.iscomplex(a)])

# Broadcasting
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print(c)
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])
print(a, '+',  b, '=')
print(a+b)
'''

# Iterating Over Array
'''
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(a)
for x in np.nditer(a):
    print(x)
b = a.T
print(b)
for x in np.nditer(b):
    print(x)

c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x)

d = b.copy(order='F')
print(d)
for x in np.nditer(d):
    print(x)

for x in np.nditer(a, order='C'):
   print(x)
for x in np.nditer(a, order='F'):
   print(x)

for x in np.nditer(a, op_flags=['readwrite']):
   x[...] = 2*x
print(a)

a = np.arange(0,60,5)
a = a.reshape(3,4)
for x in np.nditer(a, flags=['external_loop'], order='F'):
   print(x)

b = np.array([1, 2, 3, 4], dtype=int)
for x, y in np.nditer([a, b]):
   print("%d:%d" % (x, y))
'''

# Array Manipulation
'''
#Changing Shape
a = np.arange(8)
b = a.reshape(4,2)
print(a.flat[5])
print(a.flatten(order='F'))     # ndarray.flatten(order)
print(a.ravel(order='C'))       # numpy.ravel(a, order)
# Transpose Operations
print(np.transpose(a))
print(a.T)
ax = np.arange(8).reshape(2, 2, 2)
print(np.rollaxis(ax, 2))
print(np.swapaxes(ax, 2, 0))           #numpy.swapaxes(arr, axis1, axis2)
'''

# String Functions
'''
print(np.char.add(['hello', 'hi'],[' abc', ' xyz']))
print(np.char.multiply('Hello ', 3))
print(np.char.center('hello', 20, fillchar='*'))
print(np.char.capitalize('hello world'))
print(np.char.title('learn numpy tutorials'))
print(np.char.lower(['HELLO', 'WORLD']))
print(np.char.upper(['hello', 'world']))
print(np.char.split('hello how are you?'))
print(np.char.split('TutorialsPoint,Hyderabad,Telangana', sep=','))
print(np.char.splitlines('hello\nhow are you?'))
print(np.char.strip('ashok arora', 'a'))
print(np.char.strip(['arora', 'admin', 'java'], 'a'))
print(np.char.join(':', 'dmy'))
print(np.char.join([':', '-'], ['dmy', 'ymd']))
print(np.char.replace('He is a good boy', 'is', 'was'))
a = np.char.encode('hello', 'cp500')
print(a)
print(np.char.decode(a, 'cp500'))
'''

# Mathematical Functions
'''
#Trigonometric Functions
a = np.array([0, 30, 45, 60, 90])
print(np.cos(a*np.pi/180))
print(np.tan(a*np.pi/180))
print(np.sin(a*np.pi/180))

sin = np.sin(a*np.pi/180)
print(sin)
inv = np.arcsin(sin)
print(inv)
print(np.degrees(inv))
cos = np.cos(a*np.pi/180)
print(cos)
inv = np.arccos(cos)
print(inv)
print(np.degrees(inv))
tan = np.tan(a*np.pi/180)
print(tan)
inv = np.arctan(tan)
print(inv)
print(np.degrees(inv))
# Functions for Rounding( numpy.around())
a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print(np.around(a))
print(np.around(a, decimals=1))
print(np.around(a, decimals=-1))

a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(np.floor(a))
print(np.ceil(a))
'''

# Arithmetic Operations
'''
a = np.arange(9, dtype=np.float_).reshape(3, 3)
b = np.array([10, 10, 10])
print(a, ',', b)
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.divide(a, b))

a = np.array([0.25, 1.33, 1, 0, 100])   # numpy.reciprocal()
print(a)
print(np.reciprocal(a))
b = np.array([100], dtype=int)
print(np.reciprocal(b))

#numpy.power()
a = np.array([10, 100, 1000])
b = np.array([1, 2, 3])
print(np.power(a, 2))
print(np.power(a, b))
# numpy.mod()
a = np.array([10, 20, 30])
b = np.array([3, 5, 7])
print(np.mod(a, b))
print(np.remainder(a, b))
'''

# Statistical Functions
'''
# numpy.amin() and numpy.amax()
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(np.amin(a,1))
print(np.amin(a,1))
print(np.amax(a))
print(np.amax(a, axis = 0))
# numpy.ptp()
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(a)
print(np.ptp(a))
print(np.ptp(a, axis=1))
print(np.ptp(a, axis=0))

# numpy.percentile(a, q, axis)
a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print(a)
print(np.percentile(a, 20))
print(np.percentile(a,50, axis = 1))
print(np.percentile(a,50, axis = 0))

# numpy.median()
a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
# numpy.mean()
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

# numpy.average()
a = np.array([1, 2, 3, 4])
print(np.average(a))
wts = np.array([4,3,2,1])
print(np.average(a,weights = wts))
print(np.average([1,2,3, 4],weights = [4,3,2,1], returned = True))
a = np.arange(6).reshape(3,2)
wt = np.array([3, 5])
print(np.average(a, axis=1, weights=wt))

# Standard Deviation = std = sqrt(mean(abs(x - x.mean())**2))
print(np.std([1, 2, 3, 4]))
# Variance = mean(abs(x - x.mean())**2)
print(  np.var([1,2,3,4])) 
'''
# Sort, Search & Counting Functions
'''
# numpy.sort(a, axis, kind, order)
a = np.array([[3,7],[9,1]])
print(a)
print(np.sort(a), np.sort(a, axis=0))
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju",21),("anil",25),("ravi", 17), ("amar",27)], dtype = dt)
print(np.sort(a, order='name'))

# numpy.argsort()
x = np.array([3, 1, 2])
print(x)
y = np.argsort(x)
print(y)
print(x[y])
for i in y:
   print(x[i])

# numpy.lexsort()
nm = ('raju','anil','ravi','amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
ind = np.lexsort((dv, nm))
print(ind)
print([nm[i] + ", " + dv[i] for i in ind])

# numpy.argmax() and numpy.argmin()
a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print(a)
print(np.argmax(a))
print(a.flatten())
maxindex = np.argmax(a, axis=0)
print(maxindex)
maxindex = np.argmax(a, axis=1)
print(maxindex)
minindex = np.argmin(a)
print(minindex)
print(a.flatten()[minindex])

# numpy.nonzero()
a = np.array([[30,40,0],[0,20,10],[50,0,60]])
print(a)
print(np.nonzero(a))

# numpy.where()
x = np.arange(9.).reshape(3, 3)
print(x)
y = np.where(x > 3)
print(y)
print(x[y])

# numpy.extract()
condition = np.mod(x, 2) == 0
print(condition)
print(np.extract(condition, x))
'''

# Byte Swapping
'''
a = np.array([1, 256, 8755], dtype=np.int16)
print(a)
print(map(hex, a))
print(a.byteswap(True))
print(map(hex, a))
'''

# Copies & Views
'''
a = np.arange(6)
b = a
print(id(a), '&', id(b))
b.shape = 3, 2
print(a, '&', b)
# View or Shallow Copy
a = np.arange(6).reshape(3,2)
print(a)
b = a.view()
print(b)
print(id(a), ',', id(b))
b.shape = 2,3
print(a, ',', b)

# Deep Copy
a = np.array([[10, 10], [2, 3], [4, 5]])
print(a)
b = a.copy()
print(b)
print(b is a)
b[0,0] = 100
print(a, b)
'''

# Matrix Library
import numpy.matlib
'''
# numpy.matlib.empty(shape, dtype, order)
print(np.matlib.empty((2, 2)))
print(np.matlib.zeros((2, 2)))
print(np.matlib.ones((2, 2)))
# numpy.matlib.eye(n, M,k, dtype)
print(np.matlib.eye(n=3, M=4, k=1, dtype=float))
print(np.matlib.identity(5, dtype=float))
print(np.matlib.rand(3, 3))
i = np.matrix('1,2;3,4')
print(i)
j = np.asarray(i)
print(j)
'''

# Linear Algebra
'''
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(a, b)
print(np.dot(a, b))
print(np.vdot(a,b))
print(np.inner(np.array([1,2,3]),np.array([0,1,0])))
print(np.inner(a,b))
a = [[1,0],[0,1]]
b = [[4,1],[2,2]]
print(np.matmul(a,b))
b = [1,2]
print(np.matmul(a,b))
print(np.matmul(b,a))
a = np.arange(8).reshape(2,2,2)
b = np.arange(4).reshape(2,2)
print(np.matmul(a,b))
a = np.array([[1,2], [3,4]])
print(np.linalg.det(a))
b = np.array([[6,1,1], [4, -2, 5], [2,8,7]])
print(np.linalg.det(b))
print(np.linalg.inv(a))
'''

# I/O with NumPy

a = np.array([1,2,3,4,5])
np.save('outfile', a)
b = np.load('outfile.npy')
print(b)

a = np.array([1,2,3,4,5])
np.savetxt('out.txt', a)
b = np.loadtxt('out.txt')
print(b)