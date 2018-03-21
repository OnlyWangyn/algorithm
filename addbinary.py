class Solution:
    """
    @param: a: a number
    @param: b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        aleft = len(a)-1
        bleft = len(b)-1

        maxlen = max(aleft,bleft)
        result =[0 for i in range(maxlen+1)]
        carrybit = 0
        while(aleft>=0 or bleft>=0):
            if(aleft>=0 and bleft>=0):
                anum = int(a[aleft])
                bnum = int(b[bleft])
                result[maxlen] = anum + bnum + carrybit -2 if anum + bnum + carrybit > 1 else anum + bnum + carrybit
                carrybit = 1 if anum + bnum + carrybit > 1 else 0
                maxlen-=1
                aleft-=1
                bleft-=1
            elif(aleft >= 0):
                anum = int(a[aleft])
                result[maxlen] = anum + carrybit -2 if anum + carrybit > 1 else anum  + carrybit
                carrybit = 1 if anum + carrybit > 1 else 0
                maxlen-=1
                aleft-=1
            elif bleft>=0:
                bnum = int(b[bleft])
                result[maxlen] =anum + carrybit -2 if bnum + carrybit > 1 else bnum + carrybit
                carrybit = 1 if bnum + carrybit > 1 else 0
                maxlen-=1
                bleft-=1
        if carrybit >0:
            result.insert(0,1)
        return int("".join(str(c) for c in result))
solution = Solution()
print solution.addBinary("11","1")


