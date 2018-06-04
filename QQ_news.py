
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import urllib.request as urlreq
import time
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

url = 'http://games.qq.com/'
url_data = requests.get(url, headers = headers).content
url_visit = requests.get(url).text
url_decode = url_data.decode('gbk')#注意因为网页缘故，必须使用gbk解码

soup = BeautifulSoup(url_decode,'html.parser')

struct = soup.find(class_ = 'section section0') #选取到今日热闻模块
print(struct.prettify())


# In[44]:


title = struct.find_all(class_="pic_txt_list t_news_list")
print(title[1])


# In[45]:


for i in title:
    head = i.find('img')['alt']
    url_title = i.find('img')['src']
    print('标题：{}。   链接：{}\n'.format(head,url_title))
    #print(head)


# In[58]:


title1 = struct.find_all('img')#另一种方法
#print(title1)
for i in title1:
    head = i['alt']#注意此时已经找到最终的单个标签了，无需再find()了
    url_title = i['src']
    print('标题：{}。   链接：{}\n'.format(head,url_title))

