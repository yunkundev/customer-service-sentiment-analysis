# -*- coding: utf-8 -*-
"""
Created on Fri May 06 18:53:35 2016

@author: Richard
"""

def get_word(file_name):
    s = []
    f = open(file_name)
    lines = f.readlines()   
    for line in lines:
        line = line.decode("utf-8")
        line = line.replace('\n','').replace(' ','')
        s.append(line)
    f.close()
    return s

label_word = []
label_word.append(get_word('sorry_word.txt'))
label_word.append(get_word('thank_word.txt'))
label_word.append(get_word('wait_word.txt'))
label_word.append(get_word('urge_word.txt'))
label_word.append(get_word('dirty_word.txt'))
label_word.append(get_word('dear_word.txt'))
label_word.append(get_word('mode_word.txt'))
label_word.append(get_word('turn_word.txt'))
label_word.append(get_word('time_word.txt'))
label_word.append(get_word('ask_word.txt'))



def valuate(s):
    count = []
    for i in xrange(len(label_word)):
        count.append(0.0)
    for i in xrange(len(label_word)):
        for word in label_word[i]:
            count[i] += s.count(word)
    return count

#返回值为x列的字符串
def find_word(s,num):
    count = valuate(s.decode('utf-8'))
    x_line = ''
    for i in xrange(len(count)):
        f = count[i]/num
        x_line += str(f) + ' '
    return x_line

# get the dialog and judge it 
file_x = open("x_test.txt")
lines = file_x.readlines()
dialog = ''
visitor = ''
agent = ''
agent_num = 0
visitor_num = 0
count = 0
x = ''
for line in lines:
    if line[0] == '#':
        count += 1
        if count == 1:
            continue
#        print 'dialog:',count-1
#        find_word(visitor,0)
        x += find_word(visitor,1)
        x += find_word(agent,1)
        x += find_word(visitor,visitor_num)
        x += find_word(agent,agent_num)+'\n'
        dialog = '' 
        agent = ''
        visitor = ''
        visitor_num = 0
        agent_num = 0
    else:
        if line.find('Visitor') > 0:
            dialog += line.split('|')[1].split(':')[1].replace('\n',' ')
            visitor += line.split('|')[1].split(':')[1].replace('\n',' ')
            visitor_num += 1                
        elif line.find('Agent') > 0:
            dialog += line.split('|')[1].split(':')[1].replace('\n',' ')
            agent += line.split('|')[1].split(':')[1].replace('\n',' ')
            agent_num += 1
#写最后一句
x += find_word(visitor,1)
x += find_word(agent,1)
x += find_word(visitor,visitor_num)
x += find_word(agent,agent_num)+'\n'

file_output = open("x5_test.txt",'w')
file_output.write(x)
file_output.close()