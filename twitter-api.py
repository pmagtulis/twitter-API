#!/usr/bin/env python
# coding: utf-8

# # Twitter API
# 
# **Background**: Practice use of Twitter API (elevated version). Most of the code were forked from [**Linus Li**](https://github.com/LinusLTLi/Ukraine_Taiwan.git). The idea is to have a template notebook for fetching tweets using keywords.
# 
# **What you need**: You would need to sign up for a Twitter Developer account and requests for an elevated version, which should take time. For more details, check on Twitter Developer [website](https://developer.twitter.com/en/docs/developer-portal/overview).

# ## Do your imports

# In[13]:


import tweepy
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from typing import Dict, Tuple
import re, os, random, string
import json


# ## API keys

# In[14]:


def configure():
    load_dotenv()


# In[15]:


os.getenv('api_key')


# ## Get available parameters
# 
# This shows what information can be retrieved through the API.

# In[17]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

'''available parameters:
#print(i.author,i.user,i.author,i.full_text,i.created_at,
#i.contributors,i.coordinates,i.retweet_count,i.retweets,
#i.source,i.source_url,i.id,i.id_str,)
'''


# ## Query
# 
# This lays out your query search for tweets and the number of tweets you want.
# 
# **Be mindful of the tweet limits per day!**
# 
# In this example, we are searching tweets about the two candidates for Philippine presidency in the 2022 elections, Leni Robredo and Ferdinand Marcos Jr.

# In[18]:


q = ('Bongbong' and 'Leni') or ('Bongbong Marcos' and 'Leni Robredo') or ('Robredo' and 'Marcos') or ('Ferdinand Marcos' and 'Maria Leonor Robredo')


# In[19]:


number_of_tweets= 1000


# ## Set up your list of dictionaries

# In[20]:


dataset=[]
for i in tweepy.Cursor(api.search_tweets, q, tweet_mode = "extended").items(number_of_tweets):
    data={}
    data['author'] = i.author
    data['retweets'] = i.retweets
    data['tweets'] = i.full_text
    data['tweet_time'] = i.created_at #verify whether this is account cretion date or tweet time
    data['tweet_location'] = i.coordinates
    data['retweet_count'] = i.retweet_count
    data['source'] = i.source
    data['id'] = i.id
    dataset.append(data)


# In[8]:


df = pd.DataFrame(dataset)


# In[9]:


df


# ## Save df to CSV
# 
# This saves the data frame to CSV.

# In[ ]:


#df.to_csv('./output.csv', index=False)

