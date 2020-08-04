#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy,os
water_file = os.path.join('data','water.xyz')
water = numpy.genfromtxt(water_file,skip_header=2,dtype='unicode')
for i in water:
    for j in water:
        dist = numpy.sqrt((float(i[1]) - float(j[1]))**2 + (float(i[2]) - float(j[2]))**2 + (float(i[3]) - float(j[3]))**2)
        print(F'{i[0]} to {j[0]} : {dist:.4f}')


# In[ ]:





# In[ ]:




