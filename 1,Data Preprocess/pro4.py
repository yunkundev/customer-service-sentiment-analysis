# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:55:44 2016

@author: Richard
"""

f = open("Sent.txt")
train_x = []
train_y = []
test_x = []
test_y = []
cross_x = []
cross_y = []
lines = f.readlines()
count = -1
for line in lines:
    if line[0] == "#":
        count += 1
        if count%10 == 5:
            if line.split("#")[2].find('1') >= 0:
                test_y.append('1\n')
            else:
                test_y.append('0\n')
            test_x.append("#"+line.split("#")[1]+"\n")
        elif count%10 == 0:
            if line.split("#")[2].find('1') >= 0:
                cross_y.append('1\n')
            else:
                cross_y.append('0\n')
            cross_x.append("#"+line.split("#")[1]+"\n")
        else: 
            if line.split("#")[2].find('1') >= 0:
                train_y.append('1\n')
            else:
                train_y.append('0\n')
            train_x.append("#"+line.split("#")[1]+"\n")
    else:       
        if count%10 == 5:
            test_x.append(line)
        elif count%10 == 0:
            cross_x.append(line)
        else:
            train_x.append(line)
print count
f1 = open("x_test.txt",'w')
f1.write("".join(test_x))
f2 = open("y_test.txt",'w')
f2.write("".join(test_y))
f3 = open("x_train.txt",'w')
f3.write("".join(train_x))
f4 = open("y_train.txt",'w')
f4.write("".join(train_y))
f5 = open("x_cv.txt",'w')
f5.write("".join(cross_x))
f6 = open("y_cv.txt",'w')
f6.write(''.join(cross_y))

f.close
