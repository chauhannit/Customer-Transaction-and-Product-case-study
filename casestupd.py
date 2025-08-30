import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Customer=pd.read_csv("C:\\Users\\nitin\\Desktop\\Customer.csv")
print(Customer)
Transaction=pd.read_csv("C:\\Users\\nitin\\Desktop\\Transactions.csv")
print(Transaction)
Product=pd.read_csv("C:\\Users\\nitin\\Desktop\\prod_cat_info.csv")
print(Product)
Cus_tran=pd.merge(left=Customer,
                 right=Transaction,
                 left_on='customer_Id',
                 right_on='cust_id',
                 how='inner',
                 indicator=True)
print(Cus_tran)
Cus_all=pd.merge(left=Cus_tran,
                 right=Product,
                 left_on='prod_cat_code',
                 right_on='prod_cat_code',
                 how='inner')
print(Cus_all)
print(Cus_all.dtypes)
n=10
print(Cus_all.head(n))
print(Cus_all.tail(n))
data_min=Cus_all['total_amt'].min()
print(data_min)
data_max=Cus_all['total_amt'].max()
print(data_max)
median=np.percentile(Cus_all.total_amt,25)
q1=np.percentile(Cus_all.total_amt,50)
q2=np.percentile(Cus_all.total_amt,75)
print("median",median)
print("q1=",q1)
print("q2=",q2)
freq_t=pd.crosstab(index=Cus_all['Gender'],columns=Cus_all['prod_subcat'])
freq_t.columns=['Men','Women','Kid','Mobile','Computer'
                     ,'Personal Appliances','Cameras'
                     ,'Audio and video','Fiction','Academic'
                     ,'Non-fiction','Children','Comics','DIY'
                     ,'Furnishing','Kitchen','Bath'
                     ,'Tools']
freq_t.index=['Male','Female']
print(freq_t)
'''
Tax=Cus_all['Tax']
plt.hist(Tax,color='y')
plt.ylabel('frequency')
plt.show()

total_amt=Cus_all['total_amt']
plt.hist(total_amt,color='r')
plt.xlabel('Total amount')
plt.ylabel('Frequency')
plt.show()

g_count=Cus_all['Gender'].value_counts()
print(g_count)
plt.bar(g_count.index,g_count.values)
plt.show()
Cus_all['Gender'].value_counts.plot('bar')
Cus_all['Gender'].value_counts.plot('bar')
'''
'''
M=Cus_all.loc[Cus_all['Gender']=='M']
group_prod=M.groupby(['prod_cat'])['total_amt'].sum()
popular_Male=group_prod.nlargest(1)
print('The most popular product categery in male customers is :',popular_Male)
'''
'''
max_customer=Customer['city_code'].value_counts()
t=max_customer.nlargest(1)
print("City code which has maximum customer is :",t)

percent_cust=Customer['customer_Id'].count()
percent=round((t/percent_cust)*100,2)
print("Percentage of customer from the city code is {}%" .format(percent))
'''
'''
sort=Cus_all.sort_values(['total_amt','Qty'],ascending=False)
print(sort.head(1)['Store_type'])
'''
'''
df=pd.DataFrame(Cus_all)
tf=df[df.prod_cat.isin(['Electronics','Clothing']) & (df.Store_type=='Flagship store')]
tt=tf.total_amt.sum()
print("Total amount earned:",tt)
'''
'''
df=pd.DataFrame(Cus_all)
tf2=df[(df.Gender=='M') & (df.prod_cat=='Electronics')] 
tt2=tf2.total_amt.sum()
print("Gender total amount earn:",tt2)
'''
'''
df=pd.DataFrame(Cus_all)
d=df[(df.total_amt>0)]
uq=d.transaction_id.nunique()
print('Total customer have more than 10 unique transactions are:',uq)
'''
'''
df=pd.DataFrame(Cus_all)
yrr=pd.to_datetime('today').year
db=pd.DatetimeIndex(df['DOB']).year
w=db-100
x=yrr-w
y=yrr-db
df['age']=(np.where(db>yrr,x,y))
print(df)
'''