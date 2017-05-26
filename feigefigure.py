#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 08:14:46 2017

@author: foolwolf0068
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(1,10,500)
y=np.sin(x)+1
z=np.cos(x**2)+1
plt.figure(figsize=(8,4))
plt.plot(x,y,label='$\sinx+1$',color='red',linewidth=2)
plt.plot(x,z,'b--',label='$\cosx^2+1$')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('feige\'s first figure')
plt.ylim(0,2.2)
plt.legend()
plt.show()
c=np.linspace(1,10,10)
print(c)