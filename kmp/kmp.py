class KMPSolution:
    def indexOf(self,str1,str2):
        if len(str1)<len(str2):
            return -1
        nextArray = self.getNextArray(str2)
        str1Array = list(str1)
        str2Array = list(str2)
        i=0
        m=0
        while i < len(str1Array) and m < len(str2Array):
            if(str1Array[i]==str2Array[m]):
                i+=1
                m+=1
            elif nextArray[m]==-1:
                i+=1
            else:
                m = nextArray[m]
        return i-m if m == len(str2Array) else -1
    def getNextArray(self,str2):
        if len(str2)==1:
            return [-1]
        strArray = list(str2)
        next=[0 for i in range(len(str2))]
        next[0]=-1
        next[1]=0
        index = 2
        cn = 0
        while index<len(str2):
            if strArray[index-1]==strArray[cn]:
                cn+=1
                next[index]=cn
                index+=1
            elif cn > 0:
                cn=next[cn]
            else:
                next[index]=0
                index+=1
        return next
s = KMPSolution()
print s.indexOf("aaaabcxxxx","abc")