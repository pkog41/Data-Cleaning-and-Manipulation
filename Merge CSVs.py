#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install jupyterthemes


# In[22]:


from jupyterthemes import get_themes
import jupyterthemes as jt
from jupyterthemes.stylefx import set_nb_theme
#onedork | grade3 | oceans16 | chesterish | monokai | solarizedl | solarizedd
set_nb_theme("oceans16")


# In[26]:


import os
import glob
import pandas as pd
os.chdir(r"C:\Users\patrickogrady\OneDrive - Provident10\Documents\Work Stuff\Investments\NEXEN\Interactive Analytics Report")


# In[29]:


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


# In[31]:


#combine all fles in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
#export to csv
combined_csv.to_csv("combined_IAR", index=False, encoding='utf-8-sig')


# In[ ]:




