#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


page


# In[5]:


soup=BeautifulSoup(page.content)


# In[32]:


Header_tags=soup.find('span',id="From_today's_featured_article")


# In[33]:


Header_tags


# In[38]:


Header_tags.text


# In[46]:


text=[]
for i in soup.find_all('span',id="From_today's_featured_article"):
    text.append(i.text)


# In[47]:


text


# In[1]:


# Q.2) Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice) from https://presidentofindia.nic.in/former-presidents.htm and make data frame.


# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[5]:


page


# In[6]:


soup=BeautifulSoup(page.content)


# In[7]:


soup


# In[8]:


President_name=soup.find('div',class_="presidentListing")


# In[9]:


President_name


# In[10]:


President_name.text


# In[11]:


text=[]
for i in soup.find_all('div',class_="presidentListing"):
    text.append(i.text.split('(')[0].split('\n')[1])


# In[12]:


text


# In[13]:


sta=soup.find('div',class_="presidentListing")


# In[14]:


sta


# In[15]:


sta.text.split('Term of Office:')[1]


# In[16]:


Tenure=[]
for i in soup.find_all('div',class_="presidentListing"):
    Tenure.append(i.text.split('Term of Office')[1].split('\nhttp')[0].split('\n')[0])
Tenure


# In[17]:


import pandas as pd
df=pd.DataFrame({'Name':text,'Term of Office':Tenure})


# In[18]:


df


# 6) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details and make data frame-
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL

# In[19]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[20]:


page


# In[21]:


soup=BeautifulSoup(page.content)


# In[22]:


soup


# In[23]:


Paper_title=soup.find('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg")


# In[24]:


Paper_title


# In[25]:


Paper_title.text


# In[26]:


Paper_title=[]
for i in soup.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    Paper_title.append(i.text)


# In[27]:


Paper_title


# In[28]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[29]:


page


# In[30]:


soup=BeautifulSoup(page.content)


# In[31]:


soup


# In[32]:


Author=soup.find('span',class_="sc-1w3fpd7-0 dnCnAO")


# In[33]:


Author


# In[34]:


Author.text


# In[35]:


Author=[]
for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    Author.append(i.text)


# In[36]:


Author


# In[37]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[38]:


page


# In[39]:


soup=BeautifulSoup(page.content)


# In[40]:


soup


# In[41]:


Published_date=soup.find('span',class_="sc-1thf9ly-2 dvggWt")
Published_date


# In[42]:


Published_date.text


# In[43]:


Published_date=[]
for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    Published_date.append(i.text)
Published_date


# In[44]:


paper_url=('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[45]:


df=pd.DataFrame({'Paper Title':Paper_title,'Authors':Author,'Published Date':Published_date,'Paper_url':paper_url})


# In[46]:


df


# Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team andrating.
# c) Top 10 ODI bowlers along with the records of their team andrating.

# In[58]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[59]:


page


# In[60]:


soup=BeautifulSoup(page.content)


# In[61]:


soup


# In[67]:


Teams=soup.find('tr',class_="table-body")


# In[68]:


Teams


# In[69]:


Teams.text


# 7) Write a python program to scrape mentioned details from dineout.co.in and make data frame-
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[70]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[71]:


page


# In[72]:


soup=BeautifulSoup(page.content)


# In[73]:


soup


# In[82]:


Restaurant_name=soup.find('div',class_="restnt-info cursor")


# In[88]:


Restaurant_name


# In[90]:


Restaurant_name=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    Restaurant_name.append(i.text)
Restaurant_name


# In[91]:


import pandas as pd
df=pd.DataFrame({'Restaurant name':Restaurant_name})


# In[92]:


df


# In[93]:


Cuisine=soup.find('span',class_="double-line-ellipsis")


# In[94]:


Cuisine


# In[131]:


Cuisine=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    Cuisine.append(i.text.split('|')[1])
Cuisine


# In[132]:


df=pd.DataFrame({'Cuisine':Cuisine})
df


# In[99]:


Location=soup.find('div',class_="restnt-loc ellipsis")


# In[101]:


Location.text


# In[102]:


Loc=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    Loc.append(i.text)
Loc


# In[117]:


df=pd.DataFrame({'Location':Loc})
df


# In[118]:


Ratings=soup.find('div',class_="restnt-rating rating-4")
Ratings
Ratings.text


# In[119]:


Ratings=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    Ratings.append(i.text)
Ratings
df=pd.DataFrame({'Ratings':Ratings})
df


# In[120]:


Image=soup.find('img',class_="no-img")
Image


# In[121]:


Image=[]
for i in soup.find_all('img',class_="no-img"):
    Image.append(i.get('data-src'))
Image


# In[122]:


df=pd.DataFrame({'Image':Image})
df


# In[124]:


print(len(Restaurant_name),len(Cuisine),len(Loc),len(Ratings),len(Image))


# In[133]:


df=pd.DataFrame({'Restaurant_name':Restaurant_name, 'Cuisine':Cuisine,'Location':Loc, 'Ratings': Ratings, 'Image URL': Image})


# In[134]:


df


# In[ ]:




