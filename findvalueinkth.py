
def findValue(val,matrix):
    row = len(matrix)
    col = len(matrix[0])
    startrow = 0
    startcol = col -1
    while(startcol >=0 and startrow<row):
     if matrix[startrow][startcol] == val:
        return startrow,startcol
     elif matrix[startrow][startcol] > val:
         startcol-=1
     elif matrix[startrow][startcol]< val:
         startrow+=1
    return  -1,-1
matrix =[
    [1 ,5 ,7],
    [3 ,7 ,8],
    [4 ,8 ,9],
]
print findValue(4,matrix)