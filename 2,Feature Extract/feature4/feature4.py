# -*- coding: utf-8 -*-
"""
Created on Fri May 06 16:22:34 2016

@author: Richard
"""
def find_sign(dialog):
    x = []
    for i in xrange(5):
        x.append(0.0)
    for sentence in dialog:
        x[0] += sentence.count('！')
        if sentence.split('|')[1].split(':')[1].strip() == '？':
            x[1] += 1
        x[3] += sentence.count('？')
        if sentence.find('/') >= 0 or sentence.find('[') >= 0:
            x[4] += 1
    x[3] = x[3]/len(dialog)
    x[2] = x[0]/len(dialog)
    s = ''
    for i in x:
        s += str(i) +' '
    return s
    

file_input = open("x.txt")
lines = file_input.readlines()
dialog = []
visitor = []
count = 0
s = ''
for line in lines:
    if line[0] == '#':
        count += 1
        if count == 1:
            continue
        else:
            s += find_sign(dialog)
            s += find_sign(visitor)
            s += '\n'
        dialog = []
        visitor = []
    else:
        if line.find('Visitor') > 0:
            visitor.append(line.replace('\n',''))
        dialog.append(line.replace('\n',''))
s += find_sign(dialog)
s += find_sign(visitor)
s += '\n'

file_output = open("x4.txt",'w')
file_output.write(s)
file_output.close()
