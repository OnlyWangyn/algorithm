class Solution:
    """
    @param: matrix: a matrix of integers
    @param: k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        row = len(matrix)
        col = len(matrix[0])
        help=[]
        startrow = 0
        startcol =0
        while startrow < row and startcol < col:
            help.append(matrix[startrow][startcol])
            t=self.getArray(matrix,startrow,startcol)
    def getArray(self,matrix,startrow,startcol):
        row = len(matrix)
        col = len(matrix[0])
        temp = []
        while startrow+1 < row and startcol+1 < col:
            if matrix[startrow][startcol+1] < matrix[startrow+1][startcol]:
                temp.append(matrix[startrow][startcol+1])
                startcol+=1
            else:
                temp.append(matrix[startrow+1][startcol])
                startrow+=1
        return temp