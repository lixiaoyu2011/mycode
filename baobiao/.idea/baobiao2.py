#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np

head = ["name" , "li" , "a3"]
l = [[1 , 2 , 3],[4,5,6] , [8 , 7 , 9]]
print(type(l))
df = pd.DataFrame (l , columns = head)
df.to_csv ("testfoo.csv" , encoding = "utf-8")
df2 = pd.read_csv ("testfoo.csv" , encoding = "utf-8")
print (df2)