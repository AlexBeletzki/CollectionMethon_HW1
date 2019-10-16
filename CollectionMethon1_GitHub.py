#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[6]:


import getpass


# In[3]:


username = 'AlexBeletzki'


# In[7]:


password = getpass.getpass()


# In[8]:


r = requests.get('https://api.github.com/user', auth=(username, password))


# In[9]:


r.text


# In[10]:


r.json()


# In[11]:


repos = requests.get('https://api.github.com/user/repos', auth=(username, password))


# In[14]:


repos.json()[1]


# In[16]:


for repo in repos.json():
    if not repo['private']:
        print(repo['html_url'])


# In[18]:


import json


# In[26]:


with open("repos.json", "w") as write_file:
    json.dump(repos.json(), write_file)


# In[29]:


file_path = 'C:\Users\Public'


# In[ ]:


github_api_file_url = 'https://api.github.com/repos/natenka/pyneng-examples-exercises/contents/'

