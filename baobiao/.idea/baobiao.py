#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
trainfile='../data/data.xlsx'
#读取数据 指定日期为索引
data=pd.read_excel(trainfile)#读取数据，指定“日期”列为索引列
print (data.head())
print(data[u'日期'])
##################人均vv################################
data[u'播放次数对照组']
data[u'播放人数对照组']
data[u'人均vv对照组']=data[u'播放次数对照组']/data[u'播放人数对照组']
print(data[u'人均vv对照组'])

data[u'播放次数实验组']
data[u'播放人数实验组']
data[u'人均vv实验组']=data[u'播放次数实验组']/data[u'播放人数实验组']
print(data[u'人均vv实验组'])
##################人均播放时长###################################
data[u'总播放时长对照组']
data[u'播放人数对照组']
data[u'人均播放时长对照组']=data[u'总播放时长对照组']/data[u'播放人数对照组']
print(data[u'人均播放时长对照组'])

data[u'总播放时长实验组']
data[u'播放人数实验组']
data[u'人均播放时长实验组']=data[u'总播放时长实验组']/data[u'播放人数实验组']
print(data[u'人均播放时长实验组'])

#########################人均曝光######################################
data[u'曝光次数对照组']
data[u'曝光人数对照组']
data[u'人均曝光对照组']=data[u'曝光次数对照组']/data[u'曝光人数对照组']
print(data[u'人均曝光对照组'])

data[u'曝光次数实验组']
data[u'曝光人数实验组']
data[u'人均曝光实验组']=data[u'曝光次数实验组']/data[u'曝光人数实验组']
print(data[u'人均曝光实验组'])

#########################人均点击######################################
data[u'点击次数对照组']
data[u'点击人数对照组']
data[u'人均点击对照组']=data[u'点击次数对照组']/data[u'点击人数对照组']
print(data[u'人均点击对照组'])

data[u'点击次数实验组']
data[u'点击人数实验组']
data[u'人均点击实验组']=data[u'点击次数实验组']/data[u'点击人数实验组']
print(data[u'人均点击实验组'])

#########################播放完成率######################################
data[u'播放完成次数对照组']
data[u'播放次数对照组']
data[u'播放完成率对照组']=data[u'播放完成次数对照组']/data[u'播放次数对照组']
print(data[u'播放完成率对照组'])

data[u'播放完成次数实验组']
data[u'播放次数实验组']
data[u'播放完成率实验组']=data[u'播放完成次数实验组']/data[u'播放次数实验组']
print(data[u'播放完成率实验组'])

#########################vv######################################

data[u'播放次数对照组']
data[u'vv对照组']=data[u'播放次数对照组']
print(data[u'vv对照组'])

data[u'播放次数实验组']
data[u'vv实验组']=data[u'播放次数实验组']
print(data[u'vv实验组'])

#########################曝光次数######################################

data[u'曝光次数对照组']
print(data[u'曝光次数对照组'])

data[u'曝光次数实验组']
print(data[u'曝光次数实验组'])
#########################播放人数######################################

data[u'播放人数对照组']
print(data[u'播放人数对照组'])

data[u'播放人数实验组']
print(data[u'播放人数实验组'])

#########################点击人数######################################

data[u'点击人数对照组']
print(data[u'点击人数对照组'])

data[u'点击人数实验组']
print(data[u'点击人数实验组'])

#########################总播放时长######################################

data[u'总播放时长对照组']
print(data[u'总播放时长对照组'])

data[u'总播放时长实验组']
print(data[u'总播放时长实验组'])


head = ["日期","人均vv对照组","人均vv实验组","日期","人均播放时长对照组","人均播放时长实验组","日期","人均曝光对照组","人均曝光实验组"]
#head = ["日期","人均vv对照组","人均vv实验组"]
print(data[u'日期'])
df = pd.concat([data[u'日期'],data[u'人均vv对照组'] , data[u'人均vv实验组'],data[u'日期'],data[u'人均播放时长对照组'] , data[u'人均播放时长实验组'],data[u'日期'],data[u'人均曝光对照组'] , data[u'人均曝光实验组']],axis=1)
print(df)
df.to_csv("../out/out1.csv", index=False)

head2 = ["日期","人均点击对照组","人均点击实验组","日期","播放完成率对照组","播放完成率实验组","日期","vv对照组","vv实验组"]
df2 = pd.concat([data[u'日期'],data[u'人均点击对照组'] , data[u'人均点击实验组'],data[u'日期'],data[u'播放完成率对照组'] , data[u'播放完成率实验组'],data[u'日期'],data[u'vv对照组'] , data[u'vv实验组']],axis=1)
print(df2)
df2.to_csv("../out/out2.csv", index=False)

head3 = ["日期","曝光次数对照组","曝光次数实验组","日期","播放人数对照组","播放人数实验组","日期","点击人数对照组","点击人数实验组"]
df3 = pd.concat([data[u'日期'],data[u'曝光次数对照组'] , data[u'曝光次数实验组'],data[u'日期'],data[u'播放人数对照组'] , data[u'播放人数实验组'],data[u'日期'],data[u'点击人数对照组'] , data[u'点击人数实验组']],axis=1)
print(df3)
df3.to_csv("../out/out3.csv", index=False)

head4 = ["日期","总播放时长对照组","总播放时长实验组"]
df4 = pd.concat([data[u'日期'],data[u'总播放时长对照组'] , data[u'总播放时长实验组']],axis=1)
print(df4)
df4.to_csv("../out/out4.csv", index=False)