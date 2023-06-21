#!/usr/bin/env python
# coding: utf-8

# In[80]:


#Q1
get_ipython().system('pip install selenium')


# In[85]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time 
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException


# In[82]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[44]:


driver.get('https://www.amazon.in/')


# In[45]:


val=input('enter your item')


# In[46]:


search=driver.find_element(By.ID,'twotabsearchtextbox')
search.send_keys(val)


# In[47]:


find=driver.find_element(By.ID,'nav-search-submit-button')
find.click()


# In[ ]:


Q2.


# In[65]:


Product_url=[]
start=0
end=3
for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        Product_url.append(i.get_attribute('href'))
        next_button=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[30]/div/div/span/a[3]')
        time.sleep(2)


# In[66]:


len(Product_url)


# In[50]:


Brand=[]
Product_name=[]
Price=[]
Return=[]
Expected_Delivery=[]
Availability=[]
Product_url=[]


# In[56]:


for url in Product_url:
    driver.get(url)
    time.sleep(2)
    
    try:
        brand=driver.find_element(By.XPATH,'//div[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span')
        Brand.append(brand.text)
    except NoSuchElementException:
        Brand.append('-')
            


# In[58]:


Product_url=[]
start=0
end=3
for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        Product_url.append(i.get_attribute('href'))
        next_button=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[30]/div/div/span/a[3]')
        time.sleep(2)
for url in Product_url:
    driver.get(url)
    time.sleep(2)
    
    try:
        brand=driver.find_element(By.XPATH,'//div[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span')
        Brand.append(brand.text)
    except NoSuchElementException:
        Brand.append('-')
            
    try:
        Name=driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]')
        Product_name.append(Name.text)
    except NoSuchElementException:
        Product_name.append ('-')

    try:
        Rate=driver.find_element(By.XPATH,'//span[@class="a-price aok-align-center"]')
        Price.append(Rate.text)
    except NoSuchElementException:
        Price.append('-')
        
    try:
        Delivery=driver.find_element(By.XPATH,'//div[@class="a-spacing-base"]')
        Expected_Delivery.append(Delivery.text)
    except NoSuchElementException:
        Expected_Delivery.append('-')
        
    try:
        Available=driver.find_element(By.XPATH,'//span[@class="a-size-base a-color-price a-text-bold"]')
        Availability.append(Available.text)
    except NoSuchElementException:
        Availability.append('-')


# In[62]:


df=pd.DataFrame({'Brand':Brand,'Product Name':Product_name,'Price':Price,'Delivery':Expected_Delivery,'Availability':Availability})
df


# In[122]:


df.to_csv('Product_details.csv',index=False)
print('Product details saved to product_details.csv')


# In[ ]:





# Q3.

# In[47]:


driver.get('https://images.google.com/')


# In[48]:


search=driver.find_element(By.CLASS_NAME,'gLFyf')
search.send_keys('fruits')


# In[49]:


find=driver.find_element(By.CLASS_NAME,'zgAlFc')
find.click()


# In[140]:


for _ in range(5):
    driver.execute_script("window.scrollBy(0,1000)")
    
images=driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')

img_urls=[]
img_data=[]
for image in images:
    source=image.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            img_urls.append(source)
            
for i in range(len(img_urls)):
    if i>10:
        break
    print("Doenloading {0} of {1} images".format (i,10))
    response=requests.get(img_urls[i])
    file=open(r"C:\Users\Gravity\Desktop\images"+str(i)+".jpg","wb")
    file.write(response.content)


# In[145]:


driver.get('https://images.google.com/')
search=driver.find_element(By.CLASS_NAME,'gLFyf')
search.send_keys('car')


# In[148]:


find=driver.find_element(By.CLASS_NAME,'zgAlFc')
find.click()


# In[150]:


for _ in range(10):
    driver.execute_script("window.scrollBy(0,1000)")
    
images=driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')

img_urls=[]
img_data=[]
for image in images:
    source=image.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            img_urls.append(source)
            
for i in range(len(img_urls)):
    if i>10:
        break
    print("Doenloading {0} of {1} images".format (i,10))
    response=requests.get(img_urls[i])
    file=open(r"C:\Users\Gravity\Desktop\images"+str(i)+".jpg","wb")
    file.write(response.content)


# In[153]:


driver.get('https://images.google.com/')
search=driver.find_element(By.CLASS_NAME,'gLFyf')
search.send_keys('MachineLearning')
find=driver.find_element(By.CLASS_NAME,'zgAlFc')
find.click()

for _ in range(10):
    driver.execute_script("window.scrollBy(0,1000)")
    
images=driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')

img_urls=[]
img_data=[]
for image in images:
    source=image.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            img_urls.append(source)
            
for i in range(len(img_urls)):
    if i>10:
        break
    print("Doenloading {0} of {1} images".format (i,10))
    response=requests.get(img_urls[i])
    file=open(r"C:\Users\Gravity\Desktop\images"+str(i)+".jpg","wb")
    file.write(response.content)


# In[50]:


driver.get('https://images.google.com/')
search=driver.find_element(By.CLASS_NAME,'gLFyf')
search.send_keys('Guitar')
find=driver.find_element(By.CLASS_NAME,'zgAlFc')
find.click()

for _ in range(20):
    driver.execute_script("window.scrollBy(0,1000)")
    
images=driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')

img_urls=[]
img_data=[]
for image in images:
    source=image.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            img_urls.append(source)
            
for i in range(len(img_urls)):
    if i>10:
        break
    print("Doenloading {0} of {1} images".format (i,10))
    response=requests.get(img_urls[i])
    file=open(r"C:\Users\Gravity\Desktop\images"+str(i)+".jpg","wb")
    file.write(response.content)


# In[51]:


driver.get('https://images.google.com/')
search=driver.find_element(By.CLASS_NAME,'gLFyf')
search.send_keys('Cakes')
find=driver.find_element(By.CLASS_NAME,'zgAlFc')
find.click()

for _ in range(20):
    driver.execute_script("window.scrollBy(0,1000)")
    
images=driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')

img_urls=[]
img_data=[]
for image in images:
    source=image.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            img_urls.append(source)
            
for i in range(len(img_urls)):
    if i>10:
        break
    print("Doenloading {0} of {1} images".format (i,10))
    response=requests.get(img_urls[i])
    file=open(r"C:\Users\Gravity\Desktop\images"+str(i)+".jpg","wb")
    file.write(response.content)


# In[4]:


#Q4
get_ipython().system('pip install selenium')

import pandas as pd
import selenium
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import warnings
warnings.filterwarnings('ignore')

driver=webdriver.Chrome(r"C:\Users\Gravity\Desktop")
driver.get('https://www.flipkart.com/')
search=driver.find_element(By.CLASS_NAME,'_3704LK')
search.send_keys('Oneplus Nord')


# In[5]:


find=driver.find_element(By.CLASS_NAME,'L0Z3Pu')
find.click()


# In[6]:


Brand_name=[]
Smartphone_name=[]
Colour=[]
RAM=[]
ROM=[]
Primary_Camera=[]
Secondary_Camera=[]
Display_Size=[]
Battery_Capacity=[]
Price=[]
Product_url=[]

Url=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in Url:
    Product_url.append(i.get_attribute('href'))
    


# In[7]:


Url


# In[28]:


len(Product_url)


# In[12]:


Url=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in Url:
    Product_url.append(i.get_attribute('href'))
    
Smartphone_name=[]
for i in Product_url:
    driver.get(i)
    time.sleep(5)
    try:
        Phone_name=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span')
        Smartphone_name.append(Phone_name.text)
    except NoSuchElementException:
        Smartphone_name.append('Not Present')
        
        
    try:
        Colour_tag=driver.find_element(By.XPATH,'//table[@class="_14cfVK"]/tbody/tr[4]/td[2]')
        Colour.append(Colour_tag.text)
    except NoSuchElementException:
        Colour.append('Not Present')
        
    try:
        Ram_tag=driver.find_element(By.XPATH,'//div[@class="_2418kt"]/ul/li')
        RAM.append(Ram_tag.text)
    except NoSuchElementException:
        RAM.append('Not Present')
        
    try:
        Rom_tag=driver.find_element(By.XPATH,'//div[@class="_2418kt"]/ul/li')
        ROM.append(Rom_tag.text)
    except NoSuchElementException:
        ROM.append('Not Present')
        
    try:
        Prim_cam=driver.find_element(By.XPATH,'//div[@class="_2418kt"]/ul/li[3]')
        Primary_Camera.append(Prim_cam.text)
    except NoSuchElementException:
        Primary_Camera.append('Not Present')
        
    try:
        Disp=driver.find_element(By.XPATH,'//div[@class="_2418kt"]/ul/li[2]')
        Display_Size.append(Disp.text)
    except NoSuchElementException:
        Display_Size.append('Not Present')
        
    try:
        Battery=driver.find_element(By.XPATH,'//div[@class="_2418kt"]/ul/li[4]')
        Battery_Capacity.append(Battery.text)
    except NoSuchElementException:
        Battery_Capacity.append('Not Present')
        
    try:
        Rate=driver.find_element(By.XPATH,'//div[@class="_30jeq3 _16Jk6d"]')
        Price.append(Rate.text)
    except NoSuchElementException:
        Price.append('Not Present')
    


# In[25]:


max_length=max(len(Smartphone_name),len(Colour),len(RAM),len(ROM),len(Primary_Camera),len(Display_Size),len(Battery_Capacity),len(Price),len(Product_url)) 


# In[35]:


df=pd.DataFrame({'Name':Smartphone_name,'Colour':Colour,'RAM':RAM,'ROM':ROM,'Primary Cam':Primary_Camera,'Display':Display_Size,'Battery':Battery_Capacity,'Price':Price,'Url':Product_url})
df


# In[46]:


df.to_csv('Oneplus_data.csv',index=False)
print('Product details saved to Oneplus_data.csv')


# Q5.

# In[165]:


search=driver.get('https://www.googlemaps.com/')


# In[166]:


city=driver.find_element(By.ID,'searchboxinput')
city.send_keys('Delhi')


# In[167]:


find=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button')
find.click()


# In[170]:



import re
try:
    url_string=driver.current_url
    print("Url Extracted:",url_string)
    lat_lng=re.findall(r'@(.*)data',url_string)
except NoSuchElementException:
    print("lat and Long")


# In[188]:


URL=url_string.split('@')[1].split(',9')[0]


# In[189]:


URL


# In[200]:


Lat=URL[0:10]
Long=URL[11:20]
print("Lat=",Lat, "," "Long=",Long)


# Q.6

# In[34]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import requests


# In[67]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[36]:


driver.get('https://www.digit.in/')


# In[68]:


driver.get('https://www.digit.in/')


# In[69]:


find=driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[2]/span')
find.click()


# In[70]:


best=driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[2]/div[2]/div/div[1]/span[4]/strong')
best.click()


# In[71]:


GL=driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[2]/div[2]/div/div[5]/div/div[2]/a/span')
GL.click()


# In[72]:


Name=[]
Product_name=driver.find_elements(By.XPATH,'//div[@class="left_side"]')
for i in Product_name[0:7]:
    Name.append(i.text)


# In[73]:


Name


# In[94]:


#Q.6
import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = 'https://www.digit.in/top-products/best-gaming-laptops-40.html'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

laptops = soup.find_all('div', class_='TopNumbeHeading sticky-footer')

for laptop in laptops:
    name = laptop.find('div', class_='heading-wraper').text.strip()
    specs = laptop.find('div', class_='product-detail').text.strip()
    price = laptop.find('div', class_='smprice').text.strip()

    print(f'Name: {name}')
    print(f'Specifications: {specs}')
    print(f'Price: {price}')
    print('---')


# In[ ]:





# In[112]:


get_ipython().system('pip install selenium')


# In[113]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time 
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException


# In[114]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[115]:


driver.get('https://www.forbes.com/')


# In[116]:


find=driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div[1]/div/div')
find.click()


# In[117]:


Bill=driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div[1]/div/div[2]/ul/li[2]/div[1]')
Bill.click()


# In[119]:


World=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div[1]/div/div[2]/ul/li[2]/div[2]/div[3]/ul/li[1]')
World.click()


# In[120]:


Rank=[]
rank=driver.find_elements(By.XPATH,'//div[@class="Table_rank___YBhk Table_dataCell__2QCve"]')
for i in rank:
    Rank.append(i.text)
    
Name=[]
name=driver.find_elements(By.XPATH,'')


# In[ ]:





# Q8.

# In[62]:


get_ipython().system('pip install selenium')


# In[63]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time 
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException


# In[64]:


driver=webdriver.Chrome(r'C:\Users\Gravity\Desktop')


# In[65]:


driver.get('https://www.youtube.com/')


# In[66]:


search=driver.find_element(By.CLASS_NAME,'style-scope ytd-searchbox')
search.send_keys('Adipurush Trailer')


# In[67]:


find=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button/yt-icon')
find.click()


# In[69]:


MS=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
MS.click()


# In[82]:


for _ in range(500):
    driver.execute_script("window.scrollBy(0,1000)")
    Comments=[]    
    comments=driver.find_elements(By.XPATH,'//div[@class="style-scope ytd-expander"]')
    for i in comments[0:500]:
        Comments.append(i.text)
        
    Upvote=[]
    like=driver.find_elements(By.XPATH,'//span[@class="style-scope ytd-comment-action-buttons-renderer"]')
    for i in like[0:500]:
        Upvote.append(i.text)
        
    time=[]
    Time=driver.find_elements(By.XPATH,'//yt-formatted-string[@class="published-time-text style-scope ytd-comment-renderer"]')
    for i in Time[0:500]:
        time.append(i.text)
        

