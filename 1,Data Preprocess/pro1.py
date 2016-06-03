# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:26:18 2016

@author: Richard
"""
import os

root = "HouseAgent"
freq = {'1':0,'5':0,}
file_cr = open("Sent1.txt",'w')
file_cr.close
file_1 = open("Sent1.txt",'w+')
file_cr = open("Sent5.txt",'w')
file_cr.close
file_5 = open("Sent5.txt",'w+')
for fn in os.listdir(root):
    f = root + "\\" + fn
    file_input = open(f)
    index = 0
    lines = file_input.readlines()
    for i in xrange(len(lines)):
        if lines[i][0]  == '#':        
            if lines[i][1] == '1':
                freq['1'] += 1
                s = "#"+fn[4:7]
                s += "\n"    
                for j in xrange(i+1,len(lines)):
                    if lines[j][0] == '#' :
                        break
                    elif lines[j].find("http") > 0:
                        continue
                    elif lines[j].find("【") > 0:
                        continue
                    elif lines[j].find("服务") > 0 and lines[j].find("评价") >0:
                        continue
                    elif lines[j].find("评价") > 0 and lines[j].find("辛苦") >0:
                        continue
                    elif lines[j].find("您好，您的对话已接入") > 0:
                        continue
                    elif lines[j].find("/v1/Tenant") > 0:
                        continue
                    else:
                        s += lines[j]
                        
                file_1.write(s)
                
                i = j - 1;
            if lines[i][1] == '5':
                freq['5'] += 1
                s = "#"+fn[4:7]
                s += "\n"
                for j in xrange(i+1,len(lines)):
                    if lines[j][0] == '#' :
                        break
                    elif lines[j].find("http") > 0:
                        continue
                    elif lines[j].find("【") > 0:
                        continue
                    elif lines[j].find("服务") > 0 and lines[j].find("评价") >0:
                        continue
                    elif lines[j].find("评价") > 0 and lines[j].find("辛苦") >0:
                        continue
                    elif lines[j].find("您好，您的对话已接入") > 0:
                        continue
                    elif lines[j].find("/v1/Tenant") > 0:
                        continue
                    else:
                        s += lines[j]
                file_5.write(s)    
                i = j - 1;
            
    print i,index

for i in freq:
    print i,freq.get(i)
file_1.close
file_5.close