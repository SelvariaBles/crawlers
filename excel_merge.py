
# coding: utf-8

# In[11]:


import xlrd
import xlwt

biaotou=['时间','产品名称','最低价','最高价','平均价','单位','型号','生产企业','市场','区域','省','市','价格条件','备注','发改委零售限价','发改委批发限价']  
 
filelocation="C:/Users/Admin/Downloads//"  #搜索多个表格存放处 
fileform="xls"  #当前文件夹下搜索的文件名后缀  

filedestination="C:/Users/Admin/Downloads/merge//"  #将合并后的表格存放到的位置  
file="卓创_价格_MTBE_主营出厂价_全国_2017-1-1_2018-6-1" #合并后的表格名 
  
#首先查找默认文件夹下有多少文档需要整合  
import glob  
from numpy import *  
filearray=[]  
for filename in glob.glob(filelocation+"*."+fileform):  
    filearray.append(filename)  
#以上是从pythonscripts文件夹下读取所有excel表格，并将所有的名字存储到列表filearray 

print("在默认文件夹下有%d个文档"%len(filearray))  
ge=len(filearray)  
matrix = [None]*ge  
#实现读写数据  
  
#下面是将所有文件读数据到三维列表cell[][][]中（不包含表头）  
import xlrd  
for i in range(ge):  
    fname=filearray[i]  
    bk=xlrd.open_workbook(fname)  
    try:  
        sh=bk.sheet_by_name("产品的原始历史数据")  #sheet名字
    except:  
        print ("在文件%s中没有找到sheet1，读取文件数据失败,注意表格sheet的名字" %fname)  
    nrows=sh.nrows   
    matrix[i] = [0]*(nrows-1)  
      
    ncols=sh.ncols  
    for m in range(nrows-1):    
        matrix[i][m] = ["0"]*ncols  
  
    for j in range(1,nrows):  
        for k in range(0,ncols):  
            matrix[i][j-1][k]=sh.cell(j,k).value  
            
#下面是写数据到新的合并表格中  
import xlwt  
filename=xlwt.Workbook()  
sheet=filename.add_sheet("合并")  

#下面是把表头写上  
for i in range(0,len(biaotou)):  
    sheet.write(0,i,biaotou[i])  

#求和前面的文件一共写了多少行  
zh=1  
for i in range(ge):  
    for j in range(len(matrix[i])):  
        for k in range(len(matrix[i][j])):  
            sheet.write(zh,k,matrix[i][j][k])  
        zh=zh+1  
print("我已经将%d个文件合并成1个文件，并命名为%s.xls."%(ge,file))  
filename.save(filedestination+file+".xls")  

