#!/usr/bin/env python
# coding: utf-8

# In[144]:


get_ipython().system('pip install requests')


# In[227]:


import csv


# In[151]:


from bs4 import BeautifulSoup


# In[152]:


import requests


# In[153]:


source=requests.get('https://www.smallcase.com/discover/all?count=101').text


# In[154]:


soup=BeautifulSoup(source,'lxml')


# In[155]:


print(soup.prettify())


# In[156]:


smallcases=soup.find_all('a',class_='AllSmallcases__smallcasecard-link__2A7p_')


# In[157]:


for smallcase in smallcases:
    print(smallcase.text)
    print('')


# In[158]:


sub_category=requests.get("https://www.smallcase.com/smallcase/dividend-aristocrats-SCMO_0014").text


# In[159]:


soup1=BeautifulSoup(sub_category,'lxml')


# In[160]:


print(soup1.prettify())


# In[188]:


title=soup1.find('h1',class_='ellipsis SmallcaseTitle__name__3TX4_ font-medium mb8')


# In[189]:


print(title.text)


# In[229]:


csv_file=open('details.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['managed_by','small_descrp','cagr_time_period','carg_rate','volatility','overview','min_investment_amt',' launch_date','small_case',' about_manager'])


# In[230]:


for titles in title:
    managed_by=soup1.find('p', class_= 'text-13 text-normal mb12')
    print(managed_by.text)
    small_descrp=soup1.find('div', class_='SmallcaseDescription__description__3M27M text-15 lh-157 text-dark')
    print(small_descrp.text)
    cagr_time_period=soup1.find('div',class_='text-14 text-light text-left StatBox__title__3yY1q font-regular text-light')
    print(cagr_time_period.text)
    carg_rate=soup1.find('div',class_='text-green font-regular text-dark text-20 StatBox__value__2FWUJ mt8')
    print(carg_rate.text)
    volatility=soup1.find('div',class_='VolatilityLabel__volatility-tag-container__dcnic pt4 pb4 pl8 pr8 br-4 flex')
    print(volatility.text)
    overview=soup1.find('div', class_='Overview__rationale__1-Ra7 text-dark mt16 Overview__collapsed__2AHhf')
    print(overview.text)
    min_investment_amt=soup1.find('p', class_='text-20 font-regular text-dark')
    print(min_investment_amt.text)
    launch_date=soup1.find('p', class_='text-center font-regular text-dark')
    print(launch_date.text)
    small_case=soup1.find('div', class_='Statbox__value__2vZLj')
    print(small_case.text)
    about_manager=soup1.find('p',class_='ManagersCardUI__description-container-lg__XpvJV ManagersCardUI__description-container__K7Lca lh-157 text-14')
    print(about_manager.text)
    
    print('')
    csv_writer.writerow(['managed_by','small_descrp','cagr_time_period','carg_rate','volatility','overview','min_investment_amt',' launch_date','small_case',' about_manager'])
    
csv_file.close()


# In[ ]:




