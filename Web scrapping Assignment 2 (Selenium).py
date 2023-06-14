#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[3]:


driver=webdriver.Chrome(r"C:\Users\Gravity\Desktop")


# In[4]:


driver.get("https://www.naukri.com/")


# In[5]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys("Data Analyst")


# In[8]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys("Bangalore")


# In[9]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[10]:


Job_title=[]
Job_location=[]
Company_name=[]
experience_required=[]


# In[11]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    Job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    Job_location.append(location)
    
Company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Company_tags[0:10]:
    Company=i.text
    Company_name.append(Company)
    
Experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in Experience_tags[0:10]:
    Experience=i.text
    experience_required.append(Experience)


# In[12]:


print(len(Job_title),len(Job_location),len(Company_name),len(experience_required))


# In[14]:


import pandas as pd
df=pd.DataFrame({'Title':Job_title,'Location':Job_location,'Company Name':Company_name,'Experience':experience_required})


# In[15]:


df


# In[23]:


get_ipython().system('pip install selenium')


# In[35]:


get_ipython().system('pip install selenium')


# In[48]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[49]:


drivers=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[50]:


drivers.get('https://www.naukri.com/')


# In[51]:


destination=drivers.find_element(By.CLASS_NAME,'suggestor-input ')
destination.send_keys("Data Scientist")


# In[52]:


location=drivers.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
location.send_keys("Bangalore")


# In[53]:


search=drivers.find_element(By.CLASS_NAME,'qsbSubmit')
search.click()


# In[54]:


Job_title=[]
Job_location=[]
Company_name=[]
Experience_required=[]


# In[55]:


title_tags=drivers.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    Job_title.append(title)
    
location_tags=drivers.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    Job_location.append(location)
Name_tags=drivers.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Name_tags[0:10]:
    Name=i.text
    Company_name.append(Name)
Experience_tags=drivers.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in Experience_tags[0:10]:
    Experience=i.text
    Experience_required.append(Experience)


# In[56]:


print(len(Job_title),len(Job_location),len(Company_name),len(Experience_required))


# In[57]:


df=pd.DataFrame({'Job Title':Job_title,'Job Location':Job_location,'Company Name':Company_name,'Experience Req':Experience_required})
df


# In[58]:


get_ipython().system('pip install selenium')


# In[59]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings 
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[62]:


drivers=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[63]:


drivers.get('https://www.naukri.com/')


# In[65]:


designation=drivers.find_element(By.CLASS_NAME,'suggestor-input ')
designation.send_keys('Data Scientist')


# In[66]:


search=drivers.find_element(By.CLASS_NAME,'qsbSubmit')
search.click()


# In[83]:


location_filter = drivers.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/p/span[1]')
location_filter.click()


# In[84]:


Salary_f=drivers.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/p/span[1]')
Salary_f.click()


# In[88]:


Job_title=[]
Job_location=[]
Company_name=[]
Experience_required=[]


# In[89]:


Title_tags=drivers.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in Title_tags[0:10]:
    title=i.text
    Job_title.append(title)
    
Location_tags=drivers.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in Location_tags[0:10]:
    location=i.text
    Job_location.append(location)
    
Name_tags=drivers.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Name_tags[0:10]:
    Name=i.text
    Company_name.append(Name)
    
Exp_tags=drivers.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in Exp_tags[0:10]:
    exp=i.text
    Experience_required.append(exp)


# In[90]:


print(len(Job_title),len(Job_location),len(Company_name),len(Experience_required))


# In[91]:


df=pd.DataFrame({'Title':Job_title,'Location':Job_location,'Company':Company_name,'Experience':Experience_required})


# In[92]:


df


# In[94]:


get_ipython().system('pip install selenium')


# In[95]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[24]:


drivers=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[116]:


drivers.get('https://www.flipkart.com/')


# In[122]:


search=drivers.find_element(By.CLASS_NAME,'_3704LK')
search.send_keys('Sunglasses')


# In[124]:


find=drivers.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
find.click()


# 1. Brand
# 2. Product Description
# 3. Price

# In[159]:


Brand=[]
Product_description=[]
Price=[]
Offer_price=[]


# In[160]:


start=0
end=3
for page in range(start,end):
    Brand_tags=drivers.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in Brand_tags[0:100]:
        Brand.append(i.text)
   
    Product_tags=drivers.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in Product_tags[0:100]:
        Product_description.append(i.text)
        
    Price_tags=drivers.find_elements(By.XPATH,'//div[@class="_3I9_wc"]')
    for i in Price_tags[0:100]:
        Price.append(i.text)
        
    Offer_tags=drivers.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in Offer_tags[0:100]:
        Offer_price.append(i.text)
        
        next_button=drivers.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(3)


# In[161]:


print(len(Brand),len(Product_description),len(Price),len(Offer_price))


# In[162]:


df=pd.DataFrame({'Brand':Brand,'Product Description':Product_description,'Price':Price,'Offer Price': Offer_price})


# In[163]:


df


# In[26]:


get_ipython().system('pip install selenium')


# In[41]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[42]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[43]:


driver.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market')


# In[44]:


Rating=[]
Review_Summary=[]
Full_review=[]


# In[45]:


start=0
end=10
for page in range(start,end):
    Rating_tag=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in Rating_tag[0:10]:
        Rating.append(i.text)
        
    Review_tag=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in Review_tag[0:10]:
        Review_Summary.append(i.text)
        
    Full_tag=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in Full_tag[0:10]:
        Full_review.append(i.text)
        
        next_button = driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[46]:


print(len(Rating),len(Review_Summary),len(Full_review))


# In[47]:


df=pd.DataFrame({'Ratings':Rating,'Review Summary': Review_Summary,'Full Review':Full_review})


# In[48]:


df


# In[18]:


get_ipython().system('pip install selenium')


# In[19]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[101]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[102]:


driver.get('https://www.flipkart.com/')


# In[72]:


search=driver.find_element(By.CLASS_NAME,'_3704LK')
search.send_keys('sneakers')


# In[73]:


find=driver.find_element(By.CLASS_NAME,'L0Z3Pu')
find.click()


# In[74]:


Brand_Name=[]
Product_description=[]
Price=[]


# In[82]:


start=0
end=3
for page in range(start,end):
    Brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in Brand[0:50]:
        Brand_Name.append(i.text)
    
    Product=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in Product[0:50]:
        Product_description.append(i.text)
        
    Price_tag=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in Price_tag[0:50]:
        Price.append(i.text)
    
        next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)    


# In[77]:


df=pd.DataFrame({'Brand':Brand_Name,'Product':Product_description,'Price':Price})


# In[83]:


print(len(Brand_Name),len(Product_description),len(Price))


# Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then
# set CPU Type filter to “Intel Core i7” as shown in the below image:
# After

# In[84]:


get_ipython().system('pip install selenium')


# In[85]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[156]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[157]:


driver.get('https://www.amazon.in/')


# In[158]:


search=driver.find_element(By.ID,'twotabsearchtextbox')
search.send_keys('Laptop')


# In[159]:


find=driver.find_element(By.ID,'nav-search-submit-button')
find.click()


# In[160]:


filter=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/span[10]/li/span/a/span')
filter.click()


# In[161]:


Title=[]
Ratings=[]
Price=[]


# In[162]:


Title_tags=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in Title_tags[0:10]:
        Title.append(i.text)

Ratings_tags=driver.find_elements(By.XPATH,'//a[@class="a-popover-trigger a-declarative"]')
for i in Ratings_tags[0:10]:
    Ratings.append(i.text)
    
Price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in Price_tags[0:10]:
    Price.append(i.text)


# In[163]:


print(len(Title),len(Ratings),len(Price))


# In[164]:


df=pd.DataFrame({'Title':Title,'Ratings':Ratings,'Price':Price})
df


# Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpage https://www.azquotes.com/
# 2. Click on Top Quotes

# In[165]:


get_ipython().system('pip install selenium')


# In[200]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[206]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[207]:


driver.get('https://www.azquotes.com/')


# In[213]:


find=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
find.click()


# In[214]:


Quotes=[]
Author=[]
Type_of_Quotes=[]


# In[215]:


start=1
end=10
for page in range(start,end):
    Quotes_tags=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in Quotes_tags:
        Quotes.append(i.text)
    
    Author_tags=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in Author_tags:
        Author.append(i.text)
        
    Type_tags=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in Type_tags:
        Type_of_Quotes.append(i.text)
        
        next_button = driver.find_element(By.XPATH,'//li[@class="next"]')
    next_button.click()    
    time.sleep(3)


# In[216]:


print(len(Author),len(Quotes),len(Type_of_Quotes))


# In[212]:


df=pd.DataFrame({'Quotes':Quotes,'Author':Author,'Type Of Quote':Type_of_Quotes})
df


# In[3]:


get_ipython().system('pip install selenium')


# Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead,
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame.

# In[20]:


get_ipython().system('pip install selenium')


# In[21]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[22]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[23]:


driver.get(' https://www.jagranjosh.com/')


# In[27]:


find=driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div[3]/div/div[1]/header/div[3]/ul/li[3]/a')
find.click()


# In[28]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a')
search.click()


# In[29]:


Name=[]
Born_Dead=[]
Term_of_office=[]
Remarks=[]


# In[30]:


Name_tags=driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[2]/p')
for i in Name_tags:
    Name.append(i.text)

Born_tag=driver.find_elements(By.XPATH,' ')


# In[31]:


Name


# Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e.
# Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to type in the search bar ’50 most expensive cars’
# 3. Then click on 50 most expensive cars in the world..
# 4. Then scrap the mentioned data and make the dataframe.

# In[59]:


get_ipython().system('pip install selenium')


# In[60]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[61]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[62]:


driver.get(' https://www.motor1.com/')


# In[66]:


search=driver.find_element(By.CLASS_NAME,'m1-search-panel-input')
search.send_keys('50 most expensive cars')


# In[67]:


find=driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[3]/div/div/div/form/button[1]')
find.click()


# In[68]:


cars=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a')
cars.click()


# In[69]:


Car_name=[]
Price=[]


# In[57]:


Car_tags=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in Car_tags:
    Car_name.append(i.text)

Price_tags=driver.find_elements(By.XPATH,'/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/div[1]/p[4]')
for i in Price_tags:
    Price.append(i.text)


# In[58]:


Price

