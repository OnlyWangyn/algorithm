class Solution:
    def countAndSay(self,n):
        result=["1"]
        for index in range(1,n):
            next = self.getNext(result[index-1])
            result.append(next)
        return result[n-1]
    def getNext(self,numStr):
        next = []
        lastN = numStr[0]
        record={}
        for n in numStr:
            if n not in record.keys():
                record[n]=1
            else:
                record[n]+=1
            if lastN!=n:
                if lastN in record.keys():
                    next.append(str(record[lastN])+lastN)
                    record[lastN]=0
                lastN = n
        if lastN in record.keys():
            next.append(str(record[lastN])+lastN)
        return "".join(next)
s = Solution()
print s.countAndSay(9)



