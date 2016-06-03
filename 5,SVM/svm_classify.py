# -*- coding: utf-8 -*-
"""
Created on Thu May 05 21:00:52 2016

@author: Richard
"""
import numpy as np
import matplotlib.pyplot as myplot
from sklearn import svm
import math

def feature_scaling(X):
    m,n = np.shape(X)
    max_value=[]
    for j in xrange(n):
        max_value.append(0.0)
    for i in xrange(m):
        for j in xrange(n):
            if abs(X[i][j]) >= max_value[j]:
                max_value[j] = abs(X[i][j])
    for i in xrange(m):
        for j in xrange(n):
            X[i][j] = float(X[i][j])/max_value[j] 
    return X


def load(file_name1,file_name2):
    X = []
    Y = []
    #get x
    file_x = open(file_name1)
    lines = file_x.readlines()
    for line in lines:
        Array = []
        #基准
        #Array.append(1.0)
        line = line.replace('\n','')
        line = line.strip()
        x = line.split(' ')
        for i in xrange(80):
            e = x[i].replace('\n','').replace(' ','')
            value = float(e)
            Array.append(math.sqrt(abs(value)))
            Array.append(value)
            #polynomial
            Array.append(value*value)
            Array.append(value*value*value)
            Array.append(value*value*value*value)
        X.append(Array)
    #Feature Scaling
    X = feature_scaling(X)
    file_x.close()
    
    #get y
    file_y = open(file_name2)
    lines = file_y.readlines()
    for line in lines:
        Array = []
        y = line.replace('\n','').replace(' ','')
        Array.append(float(y))
        Y.append(Array)
    return X,Y
    
def sigmoid(z):
    return 1.0/(1 + np.exp(-z))

def plot_roc(h,y):
    c1 = 0
    c0 = 0
    for i in y:
        if i[0] == 1.0:
            c1 += 1
        if i[0] == 0.0:
            c0 += 1
    x = []
    y = []
    for i in xrange(100):
        TP = 0.0
        TN = 0.0
        FP = 0.0
        FN = 0.0
        valve = 0.01*i
        for j in xrange(c1):
            if h[j][1] > valve:
                TP += 1
            else:
                FN += 1
        for j in xrange(c1,c1+c0):
            if h[j][1] > valve:
                FP += 1 
            else:
                TN += 1
        TPR = TP/(TP+FN)
        FPR = FP/(FP+TN)
        x.append(FPR)
        y.append(TPR)
    myplot.plot(x,y,'r')
    myplot.xlabel("False positive rate")
    myplot.ylabel("True positive rate")
    myplot.title("ROC curve")
    myplot.grid(True)
    myplot.savefig("roc1.png",dpi=1000)
    myplot.show()
    
    count = 0.0
    print '1:',c1,'  0:',c0
    for i in xrange(c1):
        for j in xrange(c0):
            if h[i][1] > h[c1+j][1]:
                count += 1.0
            if h[i][1] == h[c1+j][1]:
                count += 0.5
    print 'AUC:',count/(c1*c0)
    

def svm_training(dataArray,labelArray):
    X = np.mat(dataArray)
    Y = np.mat(labelArray)
    m,n = np.shape(X)
    print m,n
    m,k = np.shape(Y)
    print m,k
    #use svm to classify
    #clf = svm.SVC(probability=True, kernel = 'rbf',C=300,gamma = 0.001 )    
    #clf = svm.SVC(probability=True, kernel = 'linear',C=3) 
    clf = svm.SVC(probability=True, kernel = 'poly',C=300, gamma = 0.01,degree = 2)
    #clf = svm.SVC(probability=True, kernel = 'sigmoid',C=3, gamma = 0.03)    
    clf.fit(X,Y)
    return clf    
    
def classify(X,clf):
    return clf.predict_proba(X)

def save(H):
    dic = {}
    a = np.asarray(H)
    for i in xrange(len(H)):
        dic[i+1] =  a[i][0]
    
    sort = sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
    s = ''
    for i in sort:
        #s += str(i[0]) + ' ' +str(i[1]) +'\n'
        s += str(i[0]) +'\n'
    file_output = open("sort.txt",'w')
    file_output.write(s)  
    file_output.close()
    

X,Y = load("x.txt","y.txt")
clf = svm_training(X,Y)
#h = classify(X,clf)
#plot_roc(h,Y)
X_test,Y_test = load("x_test.txt","y_test.txt")
H = classify(X_test,clf)
plot_roc(H,Y_test)
#save(H)
