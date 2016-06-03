# -*- coding: utf-8 -*-
"""
Created on Fri May 06 10:54:15 2016

@author: Richard
"""

def get_x7(dialog):
    num = 0.0
    flag = False
    for sentence in dialog:
        if sentence.find('Visitor') > 0 and flag == False:
            num += 1
        elif sentence.find('Agent') > 0:
            break
    return num
    
def get_x8(dialog):
    num = 0.0
    for sentence in dialog:
        if sentence.find('Visitor') > 0:
            num = 0.0
        elif sentence.find('Agent') > 0:
            num += 1
    return num

def get_x9(dialog,visitor_num):
    num = 0.0
    for sentence in dialog:
        if len(sentence)<10:
            num += 1
    return num/visitor_num
    
def calculate_sentence(dialog):
    x = []
    for k in xrange(10):
        x.append(0.0)
    visitor_num = 0.0
    agent_num = 0.0
    visitor_sentence = ''
    agent_sentence = ''
    visitor = []
    for sentence in dialog:
        if sentence.find("Visitor") >= 0:
            visitor_num += 1
            visitor_sentence += sentence.split(':')[1]
            visitor.append(sentence.split(':')[1])
        if sentence.find("Agent") >= 0:
            agent_num += 1
            agent_sentence += sentence.split(':')[1]
            
    x[0] = visitor_num
    x[1] = agent_num
    x[2] = visitor_num - agent_num
    x[3] = float(len(visitor_sentence))
    x[4] = float(len(agent_sentence))
    x[5] = float(len(visitor_sentence))/visitor_num
    x[6] = float(len(agent_sentence))/agent_num  
    x[7] = get_x7(dialog)
    x[8] = get_x8(dialog)
    x[9] = get_x9(visitor,visitor_num)
    r = ''    
    for i in x:
        r  += str(i) + ' '
    return r+'\n'




file_input = open('x.txt')
lines = file_input.readlines()
file_input.close()
s = ''
dialog = []
dialog_num = 0
for line in lines:
    if line[0] == '#':
        dialog_num += 1
        if dialog_num > 1:
            s += calculate_sentence(dialog)
        dialog = []
    else:
        dialog.append(line.split('|')[1].replace('\n',''))
s += calculate_sentence(dialog)        



file_output = open('x2.txt','w')
file_output.write(s)  
file_output.close() 
