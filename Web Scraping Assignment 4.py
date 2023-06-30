#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1.
get_ipython().system('pip install selenium')


# In[24]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings
warnings.filterwarnings
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException
import random


# In[34]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[35]:


driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')


# In[45]:


Name=[]
data_tags=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[2]')
for i in data_tags[0:30]:
    Name.append(i.text)
    
Artist=[]
Artist_tags=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[3]')
for i in Artist_tags[0:30]:
    Artist.append(i.text)
    
Views=[]
View_tags=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[4]')
for i in View_tags[0:30]:
    Views.append(i.text)

Upload_date=[]
date=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[5]')
for i in date[0:30]:
    Upload_date.append(i.text)
    
Rank=[]
rank=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[1]')
for i in rank[0:30]:
    Rank.append(i.text)


# In[47]:


print(len(Name),len(Artist),len(Views),len(Upload_date),len(Rank))


# In[78]:


df=pd.DataFrame({'Rank':Rank,'Name':Name,'Artist':Artist,'Views in Billion':Views,'Upload date':Upload_date})


# In[79]:


df


# In[ ]:





# In[50]:


#Q2.


# In[51]:


get_ipython().system('pip install selenium')


# In[52]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings
warnings.filterwarnings
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException
import random


# In[53]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[54]:


driver.get('https://www.bcci.tv/')


# In[55]:


find=driver.find_element(By.XPATH,'/html/body/nav/div[1]/button')
find.click()


# In[56]:


Int=driver.find_element(By.XPATH,'/html/body/nav/div[1]/div[2]/ul[1]/li[2]/a')
Int.click()


# In[74]:


Match_title=[]
title=driver.find_elements(By.XPATH,'//span[@class="matchOrderText ng-binding ng-scope"]')
for i in title:
    Match_title.append(i.text.split('-')[0])
    
Series=[]
srs=driver.find_elements(By.XPATH,'//span[@class="matchOrderText ng-binding ng-scope"]')
for i in title:
    Series.append(i.text.split(' ')[1])
    
Place=[]
plc=driver.find_elements(By.XPATH,'//span[@class="ng-binding ng-scope"]')
for i in plc:
    Place.append(i.text)
    
Date=[]
date=driver.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')
for i in date:
    Date.append(i.text)
    
Time=[]
time=driver.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
for i in time:
    Time.append(i.text)


# In[76]:


print(len(Match_title),len(Series),len(Place),len(Date),len(Time))


# In[77]:


df=pd.DataFrame({'Match Title':Match_title,'Series':Series,'Place':Place,'Date':Date,'Time':Time})
df


# In[16]:


#Q3.
get_ipython().system('pip install selenium')


# In[17]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementNotInteractableException


# In[22]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[23]:


driver.get('http://statisticstimes.com/')


# In[24]:


Economy=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/button')
Economy.click()


# In[27]:


India=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')
India.click()


# In[29]:


states=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
states.click()


# In[30]:


Rank=[]
rank=driver.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[1]')
for i in rank[0:33]:
    Rank.append(i.text)
    
State=[]
state=driver.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[2]')
for i in state[0:33]:
    State.append(i.text)
    
GDP1=[]
gdp=driver.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[4]')
for i in gdp[0:33]:
    GDP1.append(i.text)
    
GDP2=[]
gdp2=driver.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[3]')
for i in gdp2[0:33]:
    GDP2.append(i.text)
    
Share=[]
share=driver.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[5]')
for i in share[0:33]:
    Share.append(i.text)
    
GDPB=[]
gdpb=driver.find_elements(By.XPATH,'//table[@class="display dataTable"]/tbody/tr/td[5]')
for i in gdpb[0:33]:
    GDPB.append(i.text)


# In[31]:


print(len(Rank),len(State),len(GDP1),len(GDP2),len(Share),len(GDPB))


# In[32]:


df=pd.DataFrame({'Rank':Rank,'State':State,'GDP 18-19':GDP1,'GDP 19-20':GDP2,'Share':Share,'GDP in Billion':GDPB})


# In[33]:


df


# In[50]:


#Q4.
get_ipython().system('pip install selenium')


# In[77]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementNotInteractableException


# In[80]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[81]:


driver.get('https://github.com/')


# In[84]:


Menu=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[1]/div[2]/button/span/span')
Menu.click()


# In[85]:


OpenS=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')
OpenS.click()


# In[86]:


Trend=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a')
Trend.click()


# In[87]:


Repo_url=[]


# In[90]:


Repo_url=[]
url=driver.find_elements(By.XPATH,'//h2[@class="h3 lh-condensed"]/a')
for i in url:
    Repo_url.append(i.get_attribute('href'))
    time.sleep(2)


# In[91]:


Repo_url


# In[61]:


len(Repo_url)


# In[77]:


Repository_title=[]
Repo_desc=[]
Contri_count=[]
Lang=[]


# In[92]:


Repository_title=[]
for i in Repo_url:
    driver.get(i)
    time.sleep(5)
    try:
        title=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/main/div/div[1]/div[1]/div/span[1]/a')
        Repository_title.append(title.text)
    except NoSuchElementException:
        Repository_title.append('-')
        


# In[109]:


Repo_desc=[]
for i in Repo_url:
    driver.get(i)
    time.sleep(5)    
    try:
        desc=driver.find_element(By.XPATH,'//p[@class="f4 my-3"]')
        Repo_desc.append(desc.text)
    except NoSuchElementException:
        Repo_desc.append('-')


# In[105]:


Contri_count=[]
for i in Repo_url:
    driver.get(i)
    time.sleep(5)     
    try:
        count=driver.find_element(By.XPATH,'//span[@class="Counter ml-1"]')
        Contri_count.append(count.text)
    except NoSuchElementException:
        Contri_count.append('-')
        
    Language=[]
for i in Repo_url:
    driver.get(i)
    time.sleep(5) 
    try:
        language=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[2]/div/div[5]/div/ul')
        Language.append(language.text)
    except NoSuchElementException:
        Language.append('-')


# In[111]:


print(len(Language),len(Contri_count),len(Repo_desc),len(Repository_title))


# In[114]:


df=pd.DataFrame({'Repository Title': Repository_title,'Repository Description': Repo_desc,'Contributors Count': Contri_count,'Language Used':Language})
df


# In[ ]:





# In[12]:


#Q5.
get_ipython().system('pip install selenium')


# In[13]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementNotInteractableException


# In[14]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[18]:


driver.get('https:/www.billboard.com/')


# In[21]:


Menu=driver.find_element(By.XPATH,'/html/body/div[3]/header/div/div[4]/div/div[1]/div[1]/button')
Menu.click()


# In[22]:


Chart=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div/div/div/ul/li[1]/h3/a')
Chart.click()


# In[23]:


HH=driver.find_element(By.XPATH,'/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/span/a')
HH.click()


# In[24]:


Rank=[]
rank=driver.find_elements(By.XPATH,'//span[@class="c-label  a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"]')
for i in rank:
    Rank.append(i.text)


# In[33]:


Song_Name=[]
name=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li/h3')
for i in name:
    Song_Name.append(i.text)
    
Artist_n=[]
arts=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[1]')
for i in arts:
    Artist_n.append(i.text.split('\n')[1])
    
LWR=[]
lwr=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[4]')
for i in lwr:
    LWR.append(i.text)
    
Peak_rank=[]
peak=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[5]')
for i in peak:
    Peak_rank.append(i.text)
    
Weeks_on_board=[]
weeks=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[6]')
for i in weeks:
    Weeks_on_board.append(i.text)


# In[35]:


len(Artist_n)


# In[37]:


df=pd.DataFrame({'Song Name':Song_Name,'Artist Name':Artist_n,'Last Week Rank':LWR,'Peak Rank':Peak_rank,'Weeks on Board':Weeks_on_board})


# In[38]:


df


# In[39]:


#Q6.
get_ipython().system('pip install selenium')


# In[41]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup


# In[42]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[43]:


driver.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')


# In[44]:


Book_name=[]
name=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[2]')
for i in name:
    Book_name.append(i.text)
    
Author_name=[]
aname=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[3]')
for i in aname:
    Author_name.append(i.text)
    
Vol_sold=[]
vsold=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[4]')
for i in vsold:
    Vol_sold.append(i.text)
    
Publisher=[]
publish=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[5]')
for i in publish:
    Publisher.append(i.text)
    
Genre=[]
genre=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[6]')
for i in genre:
    Genre.append(i.text)


# In[45]:


df=pd.DataFrame({'Book Name':Book_name,'Author Name':Author_name,'Volume Sold':Vol_sold,'Publisher':Publisher,'Genre':Genre})


# In[46]:


df


# In[47]:


#Q7.
get_ipython().system('pip install selenium')


# In[48]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup


# In[49]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[50]:


driver.get('https://www.imdb.com/list/ls095964455/')


# In[55]:


Name=[]
name=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/h3')
for i in name:
    Name.append(i.text.split('. ')[1])
    
Year=[]
year=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/h3/span[2]')
for i in year:
    Year.append(i.text)
    
Genre=[]
genre=driver.find_elements(By.XPATH,'//span[@class="genre"]')
for i in genre:
    Genre.append(i.text)
    
Run_time=[]
time=driver.find_elements(By.XPATH,'//span[@class="runtime"]')
for i in time:
    Run_time.append(i.text)
    
Ratings=[]
ratings=driver.find_elements(By.XPATH,'//div[@class="ipl-rating-widget"]/div/span[2]')
for i in ratings:
    Ratings.append(i.text)
    
Votes=[]
votes=driver.find_elements(By.XPATH,'//span[@name="nv"]')
for i in votes:
    Votes.append(i.text)


# In[56]:


df=pd.DataFrame({'Name':Name,'Year Span':Year,'Genre':Genre,'Run time':Run_time,'Ratings':Ratings,'Votes':Votes})


# In[57]:


df


# In[58]:


#Q8.
get_ipython().system('pip install selenium')


# In[60]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import warnings
warnings.filterwarnings('ignore')
import time
from bs4 import BeautifulSoup


# In[61]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[67]:


driver.get('https://archive.ics.uci.edu/')


# In[68]:


datasets=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[1]/div/div/div/a[1]')
datasets.click()


# In[94]:


start=0
end=25
for page in range(start,end):
    Name=[]
    name=driver.find_elements(By.XPATH,'//h2[@class="truncate text-primary"]')
    for i in name:
        Name.append(i.text)
        
    
    Data_type=[]
    types=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[2]')
    for i in types:
        Data_type.append(i.text)
        
    Task=[]
    task=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[1]')
    for i in task:
        Task.append(i.text)
        
    Attribute_type=[]
    attribute=driver.find_elements(By.XPATH,'//tbody[@class="border"]/tr/td[2]')
    for i in attribute:
        Attribute_type.append(i.text)
        
    N_instances=[]
    instances=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[3]')
    for i in instances:
        N_instances.append(i.text)
        
    N_attributes=[]
    nattributes=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[4]')
    for i in nattributes:
        N_attributes.append(i.text)
    
    Year=[]
    year=driver.find_elements(By.XPATH,'//tbody[@class="border"]/tr/td[3]')
    for i in year:
        Year.append(i.text)
    
        next_button=driver.find_elements(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[2]/div[3]/div/button[2]')


# In[95]:


df=pd.DataFrame({'Dataset Name':Name,'Data_type':types,'Task':Task,'Attribute Type':Attribute_type,'No of Instances':N_instances,'No. of Attributes':N_attributes,'Year':Year})
df


# In[1]:


#Q9.
get_ipython().system('pip install selenium')


# In[2]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import warnings
warnings.filterwarnings('ignore')
import time
from bs4 import BeautifulSoup


# In[24]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[25]:


driver.get('https://www.naukri.com/hr-recruiters-consultants')


# In[32]:


recruiter=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/a/img')
recruiter.click()


# In[33]:


search=driver.find_element(By.CLASS_NAME,'suggestor-input ')
search.send_keys('Data Science')


# In[34]:


find=driver.find_element(By.CLASS_NAME,'qsbSubmit')
find.click()


# In[43]:


Name=[]
name=driver.find_elements(By.XPATH,'//div[@class="jobTupleHeader"]/div/a')
for i in name:
    Name.append(i.text)
    
Designation=[]
desgination=driver.find_elements(By.XPATH,'//div[@class="jobTupleHeader"]/div/a')
for i in desgination:
    Designation.append(i.text)
    
Company=[]
company=driver.find_elements(By.XPATH,'//div[@class="companyInfo subheading"]')
for i in company:
    Company.append(i.text)
    
Skills=[]
skill=driver.find_elements(By.XPATH,'//ul[@class="tags has-description"]')
for i in skill:
    Skills.append(i.text)
    
Location=[]
location=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location:
    Location.append(i.text)
    
    


# In[44]:


print(len(Name),len(Designation),len(Company),len(Skills),len(Location))


# In[48]:


df=pd.DataFrame({'Name':Name,'Designation':Designation,'Company':Company,'Skills':Skills,'Location':Location})


# In[49]:


df


# In[ ]:




