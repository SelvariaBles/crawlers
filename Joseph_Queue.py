
# coding: utf-8

# In[4]:


class Queue:  
    def __init__(self):  
        self.items = []  
   
 #入队操作  
    def enqueue(self, item):  
        self.items.append(item)  
   
 #出队操作  
    def dequeue(self):  
        return self.items.pop(0)  
   
  #判断队是否为空  
    def empty(self):  
        return self.size() == 0  
   
 #返回队中元素个数  
    def size(self):  
        return len(self.items) 
    
#----------------应用-------------------
def josephus(namelist, num):  #num即为num的倍数出列-1
    simqueue = Queue()  
    for name in namelist:  
        simqueue.enqueue(name)  
       #人名全部压入队  
   
    while simqueue.size() > 1:  
        for i in range(num):             #range返回从0开始的num个迭代序列  
           simqueue.enqueue(simqueue.dequeue())  
        #前N个指定人数依次出队，再依次入队  
   
        simqueue.dequeue()  
      #第N+1个出队  
   
    return simqueue.dequeue()  
  #返回第N+1个出队的人名  
   
if __name__ =='__main__':  
    print(josephus(range(5), 2))  #有range(5)队列，3的倍数出队，最后剩的数字

