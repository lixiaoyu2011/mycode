#!/user/bin/python
#-*- coding:UTF-8 -*-
import sys
import os
import jieba
from imp import reload
reload(sys)
#保存至文件
def savefile(savepath,content):
    with open(savepath,"w") as fp:
        fp.write(content)
        '''
            上面两行是python2.6以上版本增加的语法，省略了繁琐的文件close和try操作
            2.5版本需要from __future__ import with_statement
            新手可以参考这个链接来学习http://zhoutall.com/archives/325
        '''
#读取文件
def readfile(path):
    with open(path,"rb") as fp:
        content=fp.read()
    return content

def corpus_segment(corpus_path,seg_path):
    '''
        corpus_path是未分词语料库路径
        seg_path是分词后语料库存储路径
    '''
    catelist=os.listdir(corpus_path)#获取corpus_path下的所有目录'其中子目录的名字就是类别名，
                                    # 例如：train_corpus/art/21.txt中，'train_corpus/'是corpus_path，'art'是catelist中的一个成员
    # 获取每个目录（类别）下所有的文件
    for mydir in catelist:  # 这里mydir就是train_corpus/art/21.txt中的art（即catelist中的一个类别
        class_path = corpus_path + mydir +"/" #拼出分类子目录的路径如：train_corpus/art/
        seg_dir=seg_path + mydir +"/" #拼出分词后存贮的对应目录路径如：train_corpus_seg/art/

        if not os.path.exists(seg_dir):#是否存在分词目录，如果没有则创建该目录
            os.makedirs(seg_dir)
        file_list =os.listdir(class_path) # 获取未分词语料库中某一类别中的所有文本
        '''
                 train_corpus/art/中的
        21.txt,
        22.txt,
        23.txt
        ...
        file_list=['21.txt','22.txt',...]
       '''
        for file_path in file_list:
            fullname=class_path + file_path  # 拼出文件名全路径如：train_corpus/art/21.txt
            content=readfile(fullname) # 读取文件内容
            content = content.replace(bytearray('\r\n','GBK'), ''.encode('GBK'))  # 删除换行 content=content.replace(bytearray(',',''), ','.encode('GBK'))
            content = content.replace(bytearray(' ','GBK'), ''.encode('GBK'))  # 删除空行、多余的空格
            content_seg=jieba.cut(content) # 为文件内容分词
            savefile(seg_dir + file_path," ".join(content_seg))#将处理后的文件保存到分词后语料目录
            '''''此时，content里面存贮的是原文本的所有字符，例如多余的空格、空行、回车等等，
            接下来，我们需要把这些无关痛痒的字符统统去掉，变成只有标点符号做间隔的紧凑的文本内容
           '''
    print("中文语料分词结束！！！" )
'''

出现该错误往往是通过open()函数打开文本文件时，使用了‘rb’属性，如：fileHandle=open(filename,'rb'),则此时是通过二进制方式打开文件的，所以在后面处理时如果使用了str()函数，就会出现该错误，该错误不会再python2中出现。
具体解决方法有以下两种：
第一种，在open()函数中使用‘r’属性，即文本方式读取，而不是‘rb’,以二进制文件方式读取，可以直接解决问题。
第二种,在open()函数中使用‘rb’,可以在使用之前进行转换，有以下实例，
'''
''''
如果你对if __name__=="__main__":这句不懂，可以参考下面的文章
http://imoyao.lofter.com/post/3492bc_bd0c4ce
简单来说如果其他python文件调用这个文件的函数，或者把这个文件作为模块
导入到你的工程中时，那么下面的代码将不会被执行，而如果单独在命令行中
运行这个文件，或者在IDE（如pycharm）中运行这个文件时候，下面的代码才会运行。
即，这部分代码相当于一个功能测试。
如果你还没懂，建议你放弃IT这个行业。
'''

if __name__=="__main__":
    #对训练集进行分词
    corpus_path="../data/train_corpus/"  # 未分词分类语料库路径
    seg_path="../data/train_corpus_seg/" #分词后分类语料库路径
    corpus_segment(corpus_path,seg_path)
    #对测试集进行分词
    corpus_path="../data/test_corpus/"# 未分词分类语料库路径
    seg_path = "../data/test_corpus_seg/"  # 分词后分类语料库路径
    corpus_segment(corpus_path, seg_path)
