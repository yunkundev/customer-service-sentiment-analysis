# -*- coding: utf-8 -*-
"""
Created on Fri May 06 20:57:36 2016

@author: Richard
"""
def get_word(file_name):
    s = []
    f = open(file_name)
    lines = f.readlines()   
    for line in lines:
#        line = line.decode("utf-8")
        line = line.replace('\n','').replace(' ','')
        s.append(line)
    f.close()
    return s

solve_word = get_word("solve_word.txt")  
cannot_word = get_word("cannot_word.txt")


def get_x0(visitor):
    old = ''
    count = 0
    for i in visitor:
        if i ==old:
            count += 1
            old = ''
        else:
            old = i
    return float(count)
#差评批评
def get_x1(visitor):
    count = 0
    for i in visitor:
        if i.count('好评') > 0 and i.count('不') > 0:
            count += 1
        if i.count('差评') > 0 and i.count('不') <= 0:
            count += 1
        if i.count('投诉') > 0 and i.count('不') > 0:
            count += 1
        if i.count('满意') > 0 and i.count('不') <= 0:
            count += 1
    return float(count)
#好评表扬
def get_x2(visitor):
    count = 0
    for i in visitor:
        if i.count('好评') > 0 and i.count('不') <= 0:
            count += 1
        if i.count('差评') > 0 and i.count('不') > 0:
            count += 1
        if i.count('满意') > 0 and i.count('不') <= 0:
            count += 1
        if i.count('投诉') > 0 and i.count('不') > 0:
            count += 1    
    return float(count)
#问题未解决
def get_x3(agent):
    count = 0
    solve_word = get_word("solve_word.txt")  
    cannot_word = get_word("cannot_word.txt")
    for i in solve_word:
        for j in cannot_word:
            for k in agent:
                if k.count(i) > 0 and k.count(j) >0:
                    count += 1
    return float(count)
#问题解决
def get_x4(agent):
    count = 0
    solve_word = get_word("solve_word.txt")  
    cannot_word = get_word("cannot_word.txt")
    can_word = get_word("can_word.txt")
    for i in solve_word:
        for j in cannot_word:
            for c in can_word:
                for k in agent:
                    if k.count(i) > 0 and k.count(j) <= 0 and k.count(c)>0:
                        count += 1    
    return float(count)
    
def get_x(visitor,aget):
    x = []
    for i in xrange(10):
        x.append(0.0)
    x[0] = get_x0(visitor)
    x[1] = get_x1(visitor)
    x[2] = get_x2(visitor)
    x[3] = get_x3(agent)
    x[4] = get_x4(agent)
    x[5] = x[0]/len(visitor)
    x[6] = x[1]/len(visitor)
    x[7] = x[2]/len(visitor)
    x[8] = x[3]/len(visitor)    
    x[9] = x[4]/len(visitor)    
    s = ''
    for i in xrange(10):
        s += str(x[i]) + ' '
    return s + '\n'

file_input = open("x.txt")
lines = file_input.readlines()
count = 0
visitor = []
agent = []
s = ''
for line in lines:
    if line[0] == '#':
        count += 1
        if count == 1:
            continue
        s += get_x(visitor,agent)
        visitor = []
        agent = []
    else:
        l = ''
        l = line.split('|')[1].split(':')[1]
        l = l.strip()
        if line.find('Visitor') > 0:
            visitor.append(l)
        if line.find('Agent') > 0:
            agent.append(l)
s += get_x(visitor,agent)

file_output = file('x6.txt','w')
file_output.write(s)
file_output.close()