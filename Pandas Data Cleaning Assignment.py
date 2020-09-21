#!/usr/bin/env python
# coding: utf-8

# In[165]:


import pandas as pd
import numpy as np


# In[166]:


data={'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',

'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']}

test_data=pd.DataFrame(data)


# In[167]:


test_data


# In[168]:


#   1.Some values in the the FlightNumber column are missing. These numbers are
#   meant to increase by 10 with each row so 10055 and 10075 need to be put in
#   place. Fill in these missing numbers and make the column an integer column
#   (instead of a float column).


# In[169]:


test_data['FlightNumber']=test_data['FlightNumber'].interpolate()
test_data
#test_data['FlightNumber'].dtype


# In[170]:


# 2. The From_To column would be better as two separate columns! Split each
# string on the underscore delimiter _ to give a new temporary DataFrame with
# the correct values. Assign the correct column names to this temporary
# DataFrame.
temp_df=test_data['From_To'].str.split('_',expand=True)
temp_df.columns=['From','To']
temp_df


# In[171]:


#3. Notice how the capitalisation of the city names is all mixed up in this
# temporary DataFrame. Standardise the strings so that only the first letter is
# uppercase (e.g. "londON" should become "London".)
temp_df['To']=temp_df['To'].str.capitalize()
temp_df['From']=temp_df['From'].str.capitalize()
temp_df


# In[172]:


#4. Delete the From_To column from df and attach the temporary DataFrame
# from the previous questions.

test_data=test_data.join(temp_df)
test_data=test_data.drop(columns="From_To")
test_data


# In[173]:


#5. In the RecentDelays column, the values have been entered into the
# DataFrame as a list. We would like each first value in its own column, each
# second value in its own column, and so on. If there isn't an Nth value, the value
# should be NaN.

# Expand the Series of lists into a DataFrame named delays, rename the columns
# delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df
# with delays.


# In[178]:


test_data=test_data.join(pd.DataFrame(test_data['RecentDelays'].to_list(),columns=['Delay1','Delay2','Delay3']))
test_data=test_data.drop(columns="RecentDelays")


# In[179]:


test_data


# In[190]:


test_data['Airline'].str.extract('([a-zA-z]+)',expand=False)


# In[ ]:




