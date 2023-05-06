#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # visualizing Data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


# to avoid encoding error 'unicode escape'
df = pd.read_csv(r'D:\Python_Diwali_Sales_Analysis\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv', encoding = 'unicode_escape')


# In[3]:


df.shape


# In[4]:


# head() will show first 5 values
df.head(10)


# In[5]:


#info() will show the information about the data and object data type means character value
df.info()


# In[6]:


# drop unrelated blank coloumns
#inplace = TRUE means whatever we are removing it will save the data
df.drop(['Status' , 'unnamed1'], axis =1 , inplace=True)


# In[7]:


df.info()


# In[8]:


# To Check Null Value
pd.isnull(df).sum()


# In[9]:


df=df.dropna()


# In[10]:


#to drop null values
df.dropna(inplace= True)


# In[11]:


pd.isnull(df).sum()


# In[12]:


#Change the Data Type use 'as.type'
df['Amount'] = df['Amount'].astype('int')


# In[13]:


#to check the data type that actually converted into integer
df['Amount'].dtypes


# In[14]:


df.info()


# In[15]:


# if we want to check the column in the Data then we have to enter Coloumn;
df.columns


# In[17]:


#to rename any column we use dictionary
df.rename(columns = {'Marital_Status':'Shaadi'},inplace=True)


# In[18]:


# use describe function for specific columns
df[['Age','Gender','Amount']].describe()


# # Exploratory Data Analysis

# # Gender

# In[20]:


ax = sns.countplot(x='Gender' , data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


# plotting a bar chart for gender vs total amount
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Gender',y='Amount',data = sales_gen)


# # Age
# 

# In[23]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[24]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# # State

# In[29]:


# total number of orders from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(16,14)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[30]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(17,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# # Marital Status

# In[32]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[33]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power
# 
# Occupation

# In[34]:


sns.set(rc={'figure.figsize':(20,5)}) # defining plot size
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[35]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# # Product Category

# In[44]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[45]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# In[46]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[47]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# Conclusion:
# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




