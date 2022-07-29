#!/usr/bin/env python
# coding: utf-8

# In[147]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

data=pd.read_csv(r'C:\Users\HI\Downloads\Compressed\Data Science Job Salaries\ds_salaries.csv')
data.head()


# In[142]:


del data["Unnamed: 0"]
data


# In[70]:


data.info()


# In[71]:


data.isnull().sum()


# In[81]:


#highest earner for all data professions in USD in 2020

highearn1=data[data.work_year==2020]
highearn1=highearn1.groupby(['job_title','experience_level','company_size','company_location']).max()['salary_in_usd'].reset_index()
highearn1=highearn1.sort_values('salary_in_usd',ascending=False).head(10)
highearn1


# In[144]:


highearn1.plot(kind='bar',x='job_title',y='salary_in_usd',
              title='Top 10 earners in 2020',
              figsize=(15,6))


# In[82]:


#highest earner for all data professions in USD in 2021

highearn2=data[data.work_year==2021]
highearn2=highearn2.groupby(['job_title','experience_level','company_size','company_location']).max()['salary_in_usd'].reset_index()
highearn2=highearn2.sort_values('salary_in_usd',ascending=False).head(10)
highearn2


# In[85]:


highearn2.plot(kind='bar',x='job_title',y='salary_in_usd',title='top earners in 2021',figsize=(15,8))


# In[88]:


#highest earner for all data professions in USD in 2022

highearn3=data[data.work_year==2022]
highearn3=highearn3.groupby(['job_title','experience_level','company_size','company_location']).max()['salary_in_usd'].reset_index()
highearn3=highearn3.sort_values('salary_in_usd',ascending=False).head(10)
highearn3


# In[89]:


highearn3.plot(kind='bar',x='job_title',y='salary_in_usd',title='top earners in 2022',figsize=(15,8))


# In[92]:


#average earning per job title 

avgearn=data.groupby('job_title').mean()['salary_in_usd'].reset_index()
avgearn=avgearn.sort_values('salary_in_usd',ascending=False).head(10)
avgearn


# In[94]:


avgearn.plot(kind='bar',x='job_title',y='salary_in_usd',title='Average earning per job title',figsize=(15,8))


# In[168]:


#average pay of job titles per region

#starting with the US:

payus=data[data.company_location=='US']
payus=payus.groupby('job_title').mean()['salary_in_usd'].reset_index()
payus=payus.sort_values('salary_in_usd',ascending=False)
payus


# In[169]:


#comparing these values with the rest of the regions on the dataset

payout=data[data.company_location!='US']
payout=payout.groupby('job_title').mean()['salary_in_usd'].reset_index()
payout=payout.sort_values('salary_in_usd',ascending=False)
payout


# In[182]:


compare = pd.merge(payus,payout[['job_title','salary_in_usd']],on='job_title', how='left').dropna().head(10)
compare


# In[186]:


compare.plot(kind='bar',figsize=(15,8),x='job_title',title='Comparison of average pay per job title for US companies to other parts')


# In[120]:


#comparing avg pay by experience level

exp=data.groupby('experience_level').mean()['salary_in_usd'].reset_index()
exp=exp.sort_values('salary_in_usd',ascending=False)
exp


# In[188]:


exp.plot(kind='bar',figsize=(15,8),x='experience_level',y='salary_in_usd')


# In[136]:


#average pay by company size in the US
compsizeUS=data[data.company_location=='US']
compsizeUS=compsizeUS.groupby('company_size').mean()['salary_in_usd'].reset_index()
compsizeUS=compsizeUS.sort_values('salary_in_usd',ascending=False)
compsizeUS


# In[135]:


#average pay by company size outside the US

compsizeNOTUS=data[data.company_location!='US']
compsizeNOTUS=compsizeNOTUS.groupby('company_size').mean()['salary_in_usd'].reset_index()
compsizeNOTUS=compsizeNOTUS.sort_values('salary_in_usd',ascending=False)
compsizeNOTUS


# In[190]:


sizecomp = pd.merge(compsizeUS,compsizeNOTUS[['company_size','salary_in_usd']],on='company_size', how='left')
sizecomp


# In[193]:


sizecomp.plot(kind='bar',figsize=(15,8),x='company_size',title='Effect of company size on salary in US in comparison to other regions')


# In[195]:


#effect of remote work on pay

rem=data.groupby('remote_ratio').mean()['salary_in_usd'].reset_index()
rem=rem.sort_values('salary_in_usd',ascending=False)
rem

#plot
rem.plot(kind='bar',figsize=(15,8),x='remote_ratio',y='salary_in_usd')


# In[140]:


#employee residence on average pay

empres=data.groupby('employee_residence').mean()['salary_in_usd'].reset_index()
empres=empres.sort_values('salary_in_usd',ascending=False).head(10)
empres


# In[202]:


#employment type on average pay

emptype=data.groupby('employment_type').mean()['salary_in_usd'].reset_index()
emptype=emptype.sort_values('salary_in_usd',ascending=False).head(10)
emptype

#plot
emptype.plot(kind='bar',figsize=(15,8),x='employment_type',y='salary_in_usd',title='employment type on salary')

