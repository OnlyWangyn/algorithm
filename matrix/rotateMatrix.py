import numpy as np
def rotate(matrix):
    tr = 0
    tc = 0
    dr = np.shape(matrix)[0] - 1
    dc = np.shape(matrix)[1] - 1
    while tr < dr:
        rotateEdge(matrix,tr,tc,dr,dc)
        tr+=1
        tc+=1
        dr-=1
        dc-=1
    print matrix

def rotateEdge(matrix,tr,tc,dr,dc):
    times = dc-tc
    tmp=0
    i=0
    while i!=times:
        tmp=matrix[tr][tc+i]
        matrix[tr][tc+i]=matrix[dr-i][tc]
        matrix[dr-i][tc]=matrix[dr][dc-i]
        matrix[dr][dc-i]=matrix[tr+i][dc]
        matrix[tr+i][dc]=tmp
        i+=1
a = np.arange(16).reshape(4,4)
print a
rotate(a)