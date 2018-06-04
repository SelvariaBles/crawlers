
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.bilibili.com/bangumi/play/ep101767'
headers = ''

url_visit = requests.get(url).content

soup = BeautifulSoup(url_visit,'html.parser')
#soup.prettify()
#div = soup.find('div',attrs = {'class' : 'rate-score'})
#div = soup.find_all('div')
#score = div.find(class_ = 'rate-score')
div = soup.find(class_="bangumi-header report-wrap-module report-scroll-module clearfix")
print(div)


# In[36]:


url_get = 'https://bangumi.bilibili.com/review/web_api/media/play?media_id=5788'
#在网页的开发者工具里找到xhr请求，点开后查看'review'栏，找到所需的json格式，返回headers栏，以那个地址作为请求地址。

url_get_json = requests.get(url_get).json()
print(url_get_json)


# In[39]:


score = url_get_json['result']['rating']['score']
print(score)

