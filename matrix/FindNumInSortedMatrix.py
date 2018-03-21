from numpy import *
def findNumInSortedMatrix(matrix,num):
    row = shape(matrix)[0]
    col = shape(matrix)[1]
    rowIndex = 0
    colIndex=col-1
    while rowIndex<row and colIndex>=0:
        if(num>matrix[rowIndex][colIndex]):
            rowIndex+=1
        elif num < matrix[rowIndex][colIndex]:
            colIndex-=1
        else:
            return True
    return False
a = [ [ 0, 1, 2, 3, 4, 5, 6 ],
[ 10, 12, 13, 15, 16, 17, 18 ],
[ 23, 24, 25, 26, 27, 28, 29 ],
[ 44, 45, 46, 47, 48, 49, 50 ],
[ 65, 66, 67, 68, 69, 70, 71 ],
[ 96, 97, 98, 99, 100, 111, 122 ],
[ 166, 176, 186, 187, 190, 195, 200 ],
[ 233, 243, 321, 341, 356, 370, 380 ]
]
print findNumInSortedMatrix(a,233)