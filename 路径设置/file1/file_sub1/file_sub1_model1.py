# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:05:55 2020

@author: zhanghao354
"""

def file1_sub1_model1_fun():
    print('文件名为：file1_sub1_model1')
    
#file1_sub1_model1_fun()

#print('------------------')


#import sys
#sys.path.append("C:\\Users\\zhanghao354\\Jupyter notebook\\Python学习\\路径设置")

import model1
model1.model1_fun()


from file2 import file2_model1
file2_model1.file2_model1_fun()
