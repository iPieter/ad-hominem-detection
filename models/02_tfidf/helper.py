
# coding: utf-8

# In[3]:


import pandas as pd


# In[9]:


def get_data():
    return pd.read_csv('../../data/merged_datasets.csv', usecols=(['body', 'isAdHominem']))

