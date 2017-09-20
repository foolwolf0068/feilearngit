#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:26:56 2017
小甲鱼视频 Jy30
@author: foolwolf0068
"""

import pickle
filename = "record.txt"
pickle_file = open(filename)
contents = pickle.load(pickle_file)
pickle_file.close()
