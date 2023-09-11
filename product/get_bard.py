#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().system('pip install --upgrade bardapi')


# In[14]:


from bardapi import Bard
import os

os.environ['_BARD_API_KEY']="WQhTgQ1OiMq-ApJSTUj45Ebky53k-d6QOikRppJIZGVV54LnRh7zhSacZbDyYC3VyqgPEw."
q = input('メッセージを入力してください: ')

ans = Bard().get_answer(f'{q}')['content']
print(ans, end='')

