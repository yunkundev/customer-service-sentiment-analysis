# -*- coding: utf-8 -*-
"""
Created on Thu May 05 09:58:26 2016

@author: Richard
"""
import jieba

def get_word(file_name):
    s = []
    f = open(file_name)
    lines = f.readlines()   
    for line in lines:
        line = line.replace('\n','').replace(' ','')
        line = line.decode('utf-8')
        s.append(line)
    f.close()
    return s
    
# get the word in different sensiment
negetive_evaluate = get_word("negetive_evaluate.txt")
negetive_emotion = get_word("negetive_emotion.txt")
positive_evaluate = get_word("positive_evaluate.txt")
positive_emotion = get_word("positive_emotion.txt")
over_word = get_word("over_word.txt")


def valuate(s):
    word_list = jieba.cut(s,cut_all=True)
    count = []    
    for i in xrange(5):
        count.append(0.0)
    for word in word_list:
        if negetive_evaluate.count(word) > 0:
            count[0] += 1
        elif negetive_emotion.count(word) > 0:
            count[1] += 1
        elif positive_evaluate.count(word) > 0:
            count[2] += 1
        elif positive_emotion.count(word) > 0:
            count[3] += 1
        elif over_word.count(word) > 0:
            count[4] += 1
    return count        
    
#返回值为x列的字符串
def find_word(s,num):
    count = valuate(s.decode('utf-8'))
    x_line = ''
    for i in xrange(5):
        f = count[i]/num
        x_line += str(f) + ' '
    return x_line


# get the dialog and judge it 
file_x = open("x_cv.txt")
lines = file_x.readlines()
dialog = ''
visitor = ''
agent = ''
num = 0
visitor_num = 0
count = 0
x = ''
for line in lines:
    if line[0] == '#':
        count += 1
        if count == 1:
            continue
        print 'dialog:',count-1
#        find_word(visitor,0)
        x += find_word(visitor,1)
        x += find_word(agent,1)
        x += find_word(visitor,visitor_num)
        x += find_word(dialog,num)+'\n'
        dialog = '' 
        agent = ''
        visitor = ''
        visitor_num = 0
        num = 0
    else:
        if line.find('Visitor') > 0:
            dialog += line.split('|')[1].split(':')[1].replace('\n',' ')
            visitor += line.split('|')[1].split(':')[1].replace('\n',' ')
            visitor_num += 1            
            num += 1     
        elif line.find('Agent') > 0:
            dialog += line.split('|')[1].split(':')[1].replace('\n',' ')
            agent += line.split('|')[1].split(':')[1].replace('\n',' ')
            num += 1
#写最后一句
x += find_word(visitor,1)
x += find_word(agent,1)
x += find_word(visitor,visitor_num)
x += find_word(dialog,num)+'\n'

file_output = open("x1_cv.txt",'w')
file_output.write(x)
file_output.close()
