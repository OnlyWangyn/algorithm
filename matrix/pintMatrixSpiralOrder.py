#encoding=utf-8
from numpy import *

def spiralOrderPrint(matrix):
    tr=0
    tc=0
    dr=shape(matrix)[0]-1
    dc=shape(matrix)[1]-1
    while tr <= dr and tc <=dc:
        printEdge(matrix,tr,tc,dr,dc)
        tr+=1
        tc+=1
        dr-=1
        dc-=1
def printEdge(matrix,tr,tc,dr,dc):#tr左上角行 tc左上角的列 dr右下角行号 dc右下角列
    if tr == dr:#只有一行的情况
        index=tc
        while index <= dc:
            print matrix[tr][index]
            index+=1
    elif tc==dc:#只有一列的情况
        index = tr
        while index<=dr:
            print matrix[index][tc]
            index+=1
    else:
        currentR = tr
        currentC = tc
        while currentC!=dc:
            print matrix[tr][currentC]
            currentC+=1
        while currentR!=dr:
            print matrix[currentR][dc]
            currentR+=1
        while currentC!=tc:
            print matrix[dr][currentC]
            currentC-=1
        while currentR!=tr:
            print matrix[currentR][tc]
            currentR-=1

a = arange(15).reshape(3,5)
m = mat(a)
print a

spiralOrderPrint(a)
