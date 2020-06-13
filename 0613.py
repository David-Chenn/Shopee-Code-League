#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import datetime

#讀csv檔，存成dataframe物件
order = pd.read_csv('order_brush_order.csv')


# In[2]:


unique_shopid_list = order.shopid.unique() # get unique shopid
dfList = [] # list of dateframe


# In[ ]:


#id = unique_shopid_list[0]
for id in unique_shopid_list:
    orderId = list()
    shopId = list()
    userId = list()
    eventTime = list()

    #check each data, gether datas in the lists for the same shop id
    for i in range(len(order)):
        if (id == order['shopid'][i]):
            orderId.append(order['orderid'][i])
            shopId.append(order['shopid'][i])
            userId.append(order['userid'][i])
            eventTime.append(datetime.strptime(order['event_time'][i], "%Y-%m-%d %H:%M:%S")) # 轉換成datetime物件

    # create dataframe refer to shopid
    df = pd.DataFrame({"orderid": orderId, "shopid": shopId, "userid": userId, "event_time": eventTime})
    
    # order by time
    df = df.sort_values(by="event_time", ascending=True)
    print(df)
    
    #put dataframe in dfList
    dfList.append(df)

    #initiate lists
    orderId = []
    shopId = []
    userId = []
    eventTime = []


# In[ ]:


print(dfList)


# In[ ]:


def concentrate(data, startIndex, endIndex):
    
    ordNum = endIndex - startIndex + 1 # total orders
    userSet = set(data['userid'][startIndex:endIndex+1])
    userNum = len(userSet)
    
    return ordNum / userNum
    


# In[ ]:


for eachDF in dfList:
    START = True
    start,end = 0, 0
    start_time = eachDF['event_time'][0]
    end_time = eachDF['event_time'][0]
    for i in range(len(eachDF)):
        if START:
            start = i
            start_time = eachDF['event_time'][i]
            print(start_time)
            START = False
        else:
            if (eachDF['event_time'][i] - start_time).seconds > 3600:
                end = i-1
                end_time = eachDF['event_time'][i-1]
                print(end_time)
                rate = concentrate(eachDF, start, end)
                print(rate)
                #if rate >= 3: #order brushing
                #else: #no order brushing
                    
                START = True
                
        
        

