# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 13:21:45 2019

@author: wzy11
"""
import pandas as pd
import os
import matplotlib.pyplot as plt

#读取数据
csv_path='D:\MyBlogs\Machine Learning Project Simulation'
train_data=pd.read_csv(os.path.join(csv_path,'train.csv'))
test_data=pd.read_csv(os.path.join(csv_path,'test.csv'))

#观察数据结构
#print(train_data.head())
#train_data.info()
#print(train_data['Pclass'].value_counts())
print(train_data.describe())

fig = plt.figure()
f1= fig.add_subplot(2,1,1) 
f2= fig.add_subplot(2,1,2) 
figsize=(40,40)
train_data.groupby('Ticket').PassengerId.count().plot(kind='bar',ax=f1,figsize=figsize)
t1=pd.crosstab(train_data.Ticket, train_data.Survived,margins=False)
t2=t1.div(t1.sum(1).astype(float),axis=0).plot(kind='bar',ax=f2,figsize=figsize)























