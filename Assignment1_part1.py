#!/usr/bin/env python
# coding: utf-8

# In[5]:


class ListDivideException(Exception):
    pass


def listDivide(numbers, divide=2):
    count=0
    for i in numbers:
        if i % divide == 0:
            count+=1
    return count

    
def testListDivide():
    try:        
        print(listDivide([1,2,3,4,5]))
        print(listDivide([2,4,6,8,10]))
        print(listDivide([30,54,63,98,100], 10))
        print(listDivide([]))
        print(listDivide([1,2,3,4,5], 1))
    except ListDivideException as err:
        print("error occur", err.msg)
        raise

testListDivide()


# In[ ]:




