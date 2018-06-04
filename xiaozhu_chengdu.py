
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import time
import random

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

url = "http://cd.xiaozhu.com/"
url_visit = requests.get(url,headers = headers).content #bytes型数据
#url_visit = requests.get(url,headers = headers).text #str型数据
#url_visit = requests.get(url).content #不使用代理时写法
#type(url_visit)

soup = BeautifulSoup(url_visit, 'html.parser')
title = soup.find_all('ul',attrs={'class':"pic_list clearfix"})
#title = soup.find_all(class_="resule_img_a")
#type(title)#find_all返回的类型是列表(bs4.element.ResultSet),find返回的是tag，见下个cell
#print(title.prettify())


# In[43]:


title = soup.find_all('ul',attrs={'class':"pic_list clearfix"})
title2= soup.find('ul',attrs={'class':"pic_list clearfix"})
type(title2)
type(title[0])


# In[46]:


title[0].find('a')['href']


# In[60]:


#title2.find_all('a')['href']
print(title2.prettify())


# In[92]:


house = title2.find_all('li')
for each_house in house:
    link_url = each_house.find('a')['href']
    link = requests.get(link_url,headers = headers).content
    soup2 = BeautifulSoup(link,'html.parser')
    print(link_url)
    time.sleep(random.randint(8,44))
    #house_title0 = soup2.find('div',attrs = {'class':'pho_info'})
    #house_title =house_title0.find('em').get_text()
    house_title =soup2.find('title').get_text()
    address_h = soup2.find(class_="pho_info")
    address = address_h.find('p')['title']
    score = soup2.find(class_="score-rate").get_text()
    #print(house_title)

    with open('house.txt','a') as f:#a是追加写入，'w'是覆盖写入
        f.write('房子名称：{}；\n链接：{}；\n地址：{}；\n评分：{}\n\n'.format(house_title,link_url,address,score))

