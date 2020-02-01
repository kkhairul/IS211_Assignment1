#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Book:
    author = ""
    title = ""

    def __init__(self, title, author):        
        self.title = title
        self.author = author

    def display(self):        
        return  self.title+", written by "+self.author


# In[7]:


book1 = Book("'Of Mice and Men'","John Steinbeck")
book2 = Book("'To Kill a Mockingbird'","Harper Lee")

print(book1.display())
print(book2.display())


# In[ ]:




