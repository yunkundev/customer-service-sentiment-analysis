# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:55:44 2016

@author: Richard
"""

f = open("Sent1.txt")

lines = f.readlines()
s = ""
lis = []
v = ""
a = ""
sent = ""
count = 0
for line in lines:
    if line[0] == "#":
        if len(v)>10 and len(a)>10:
            count += 1
            lis.append(sent)            
        sent = line.replace("\n","")+"#1"+"\n"
        v = ""
        a = ""
    else:
        sent = sent + line
        if line.find("Visitor") > 0:
            s = line.split("|")[1]
            v += s.split(":")[1].replace("\n","")

        if line.find("Agent") > 0:
            s = line.split("|")[1]
            a += s.split(":")[1].replace("\n","")
if len(v)>5 and len(a)>5:
    lis.append(sent)
print count




f = open("Sent5.txt")

lines = f.readlines()
s = ""
v = ""
a = ""
sent = ""
count = 0
for line in lines:
    if line[0] == "#":
        if len(v)>10 and len(a)>10:
            count += 1
            lis.append(sent)
        sent = line.replace("\n","")+"#5"+"\n"
        v = ""
        a = ""
        
    else:
        sent = sent + line
        if line.find("Visitor") > 0:
            s = line.split("|")[1]
            v += s.split(":")[1].replace("\n","")

        if line.find("Agent") > 0:
            s = line.split("|")[1]
            a += s.split(":")[1].replace("\n","")
if len(v)>5 and len(a)>5:
    lis.append(sent)
print count

file_output = open("Sent.txt",'w')
file_output.write("")
file_output.close
file_output = open("Sent.txt",'w+')
for i in xrange(len(lis)):
    file_output.write(lis[i])
file_output.close()
f.close()