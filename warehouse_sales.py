#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv(r'C:\Users\AAKRITI\Downloads\Warehouse_and_Retail_Sales.csv', encoding = 'unicode_escape')


# In[3]:


df.head(10)


# In[4]:


df.describe()


# In[5]:


df.isna().sum()


# In[6]:


df.dropna(inplace=True)


# In[7]:


duplicates = df[df.duplicated(subset=['YEAR', 'MONTH', 'SUPPLIER', 'ITEM CODE', 'ITEM DESCRIPTION', 'ITEM TYPE', 'RETAIL SALES', 'RETAIL TRANSFERS', 'WAREHOUSE SALES'])]


# In[8]:


print(duplicates)


# In[9]:


df.shape


# In[10]:


negative_retail = (df['RETAIL SALES'] < 0).sum()
negative_transfer = (df['RETAIL TRANSFERS'] < 0).sum()
negative_warehouse = (df['WAREHOUSE SALES'] < 0).sum()

print(f'Number of negative values for retail sales: {negative_retail}')
print(f'Number of negative values for retial transfers: {negative_transfer}')
print(f'Number of negative values for warehouse sales: {negative_warehouse}')


# In[11]:


# Example: Taking the absolute value
df['RETAIL SALES'] = df['RETAIL SALES'].abs()
# Example: Taking the absolute value
df['WAREHOUSE SALES'] = df['WAREHOUSE SALES'].abs()
df['RETAIL TRANSFERS'] = df['RETAIL TRANSFERS'].abs()


# In[12]:


negative_retail = (df['RETAIL SALES'] < 0).sum()
negative_transfer = (df['RETAIL TRANSFERS'] < 0).sum()
negative_warehouse = (df['WAREHOUSE SALES'] < 0).sum()

print(f'Number of negative values for retail sales: {negative_retail}')
print(f'Number of negative values for retial transfers: {negative_transfer}')
print(f'Number of negative values for warehouse sales: {negative_warehouse}')


# In[13]:


df['TOTAL SALES'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']
df.groupby('YEAR').agg({'RETAIL SALES': 'sum', 'WAREHOUSE SALES': 'sum', 'TOTAL SALES': 'sum'})
total_sales_by_year = df.groupby('YEAR').agg({'RETAIL SALES': 'sum', 'WAREHOUSE SALES': 'sum', 'TOTAL SALES': 'sum'})
total_sales_by_year.plot(kind='bar')


# In[14]:


total_sales_by_supplier = df.groupby('SUPPLIER')['TOTAL SALES'].sum()
top_5_suppliers = total_sales_by_supplier.nlargest(5)
print(top_5_suppliers)


# In[15]:


total_sales_by_item = df.groupby(['ITEM CODE', 'ITEM DESCRIPTION', 'ITEM TYPE'])['TOTAL SALES'].sum()
top_10_items = total_sales_by_item.nlargest(10)
print(top_10_items.reset_index())


# In[16]:


monthly_average_sales = df.groupby(['YEAR', 'MONTH']).agg({'RETAIL SALES': 'mean','WAREHOUSE SALES': 'mean'})
print(monthly_average_sales)
monthly_average_sales.plot(kind='bar')


# In[30]:


item_sales_type = df.groupby(['ITEM CODE', 'ITEM TYPE']).agg({'TOTAL SALES': 'sum'}).reset_index()
item_sales_ranked = item_sales_type.sort_values(by='TOTAL SALES', ascending=False)
top_5_items = item_sales_ranked.head(5)
print(top_5_items[['ITEM CODE', 'ITEM TYPE', 'TOTAL SALES']])
plt.figure(figsize=(6, 3))
plt.bar(top_5_items['ITEM CODE'], top_5_items['TOTAL SALES'], color='green')


# In[ ]:




