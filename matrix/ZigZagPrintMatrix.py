from numpy import *
def zigZagPrintMatrix(matrix):
    row = shape(matrix)[0]
    col = shape(matrix)[1]
    tr = 0
    tc = 0
    dr = 0
    dc = 0
    direction=False
    while tr < row and tc < col:
        printLevel(matrix,tr,tc,dr,dc,direction)
        tr=tr+1 if tc==col-1 else tr
        tc=tc if tc ==col-1 else tc+1
        dc = dc+1 if dr==row-1 else dc
        dr = dr if dr==row-1 else dr+1
        direction = not direction

def printLevel(matrix,tr,tc,dr,dc,f):
    if f:
        while tr<=dr:
            print matrix[tr][tc]
            tr+=1
            tc-=1
    else:
        while dc<=tc:
            print matrix[dr][dc]
            dr-=1
            dc+=1
a =  [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12 ] ];
zigZagPrintMatrix(a)