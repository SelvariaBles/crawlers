
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://price.sci99.com/view/priceview.aspx?pagename=energyview&classid=349&linkname=mtbe&RequestId=d49c30f54cb20b26')
browser.find_element_by_xpath('//*[@id="LogInPart1_SciName"]').send_keys('jusure2016')
browser.find_element_by_xpath('//*[@id="LogInPart1_SciPwd"]').send_keys('jusure2017')
browser.find_element_by_xpath('//*[@id="LogInPart1_IB_Login"]').click()
browser.maximize_window() 
time.sleep(4)

#table = browser.find_element_by_id('divContents')
table = browser.find_elements_by_tag_name('tr')
#print(table)

oil_id = []
for tr_id in table:
    img_id = tr_id.get_attribute("id")
    if img_id:
        oil_id.append(img_id)
    else:
        pass

time.sleep(4)
browser.maximize_window() #最大化浏览器

small_list = [oil_id[i:i+4] for i in range(0,len(oil_id),4)]#[[0,1,2,3],[4,5,6,7]....]
for id_list in small_list:
    for id in id_list:
        browser.find_element_by_xpath('//*[@id="img{}"]'.format(id)).click()#选择需下载的信息
        time.sleep(1)

    time.sleep(2)

    browser.find_element_by_xpath('//*[@id="basket_close"]/a').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="txtLineStartDate"]').clear()#清空起始日期
    browser.find_element_by_xpath('//*[@id="txtLineStartDate"]').send_keys('2017-01-01')
    browser.find_element_by_xpath('//*[@id="boxhistorylink"]/b').click()#此处是查看历史数据链接，无图标，但需要选择日期（2017-01-01）
    browser.switch_to_window(browser.window_handles[-1])#0是原始界面，-1是新界面。之后的按1,2...类推，大概...
    time.sleep(4)#
    #browser.find_element_by_xpath('//*[@id="form1"]/div[6]/div[1]/ul/li[4]/a').click()#选择到一年内的数据
    browser.find_element_by_xpath('//*[@id="lbTOExcel_original"]').click()
    browser.switch_to_window(browser.window_handles[0])#返回首页重新选取
    browser.find_element_by_xpath('//*[@id="basket_close"]/div/div[1]/div[3]/a[2]/b').click()#清空数据
    browser.find_element_by_xpath('//*[@id="basket_close"]/a').click()#将点开的界面点掉

