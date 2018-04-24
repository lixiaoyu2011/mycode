#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
csvs = []
for file in os.listdir("../out"):
        csvs.append(file)
print(csvs)

fout=open("../data/combined_iso.csv","a")

for file in csvs:
    f = open("../out/"+file)
    print(f)
    for line in f:
         fout.write(line)
    f.close() # 关闭文件
fout.close()