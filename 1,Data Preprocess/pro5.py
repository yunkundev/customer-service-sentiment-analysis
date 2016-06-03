f = open('x_train.txt')
lines = f.readlines()
count = 0
s = ''
c = []
c1 = 0
c2 = 0
for line in lines:
    if line[0] == '#':
        count += 1
        if count <= 1:
            s = line.replace('\n','')+'#'+str(count)+'\n'
        elif count <= 1481:
            c.append(s)
            c1 += 1
            s = line.replace('\n','')+'#'+str(count)+'\n'
        else:
            
            if count%25 == 0:
                c.append(s)
                c2 += 1
                if c2 == 1480:
                    break
            s = line.replace('\n','')+'#'+str(1480+c2+1)+'\n'
    else:
        s += line
print c1
print c2
file_output = open('x.txt','w')
file_output.write(''.join(c))
file_output.close()

f = open("y_train.txt")
lines = f.readlines()
out = []
for line in lines:
    if line[0] == '1':
        out.append('1\n')
    if c1 > 0:
        c1 -= 1
        out.append('0\n')
file_output = open('y.txt','w')
file_output.write(''.join(out))
file_output.close()




