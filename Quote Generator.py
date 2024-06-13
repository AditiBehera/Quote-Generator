#!/usr/bin/env python
# coding: utf-8

# In[33]:


pip install python-docx


# In[48]:


import random
from docx import Document


# In[49]:


def load_quotes(file_path):
    document = Document(file_path)
    quotes = [para.text for para in document.paragraphs if para.text.strip()]
    return quotes


# In[50]:


def generate_quote(quotes):
    quote = random.choice(quotes)
    print(quote)


# In[53]:


file_path = r"C:\Users\Administrator\Desktop\MS Files\Quotes- Python project.docx"
quotes = load_quotes(file_path)


# In[54]:


generate_quote(quotes)


# In[ ]:




