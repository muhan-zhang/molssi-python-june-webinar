#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
md_file = os.path.join('data','03_Prod.mdout')
outfile = open(md_file,'r')
md_data = outfile.readlines()
outfile.close()
etot_file = open('Etot.txt','w+')
for line in md_data:
    if 'Etot' in line:
        etot_line = line
        etot_energy = etot_line.split()[2]
        etot_file.write(F'{etot_energy}\n')
etot_file.close()


# In[ ]:




