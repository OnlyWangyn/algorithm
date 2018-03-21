def manacherString(str):
    strlist= list(str)
    length = len(str)*2 +1
    res=[]
    index = 0
    for i in range(length):
        if i & 1==0 :
            res.append("#")
        else:
            res.append(strlist[index])
            index+=1
    return res
def mancher(str):
    if len(str)<1:
        return 0
    mArray = manacherString(str)
    r = -1
    c = -1
    maxvalue=0
    pArray=[0 for i in range(len(mArray))]
    for index in range(len(mArray)):
        pArray[index]= min(2*c -index,r-index) if r > index else 1
        while index+pArray[index]<len(mArray) and index-pArray[index] > -1:
            if mArray[index+pArray[index]] == mArray[index-pArray[index]]:
                pArray[index]+=1
            else:
                break
        if index+pArray[index] > r:
            r = index+pArray[index]
            c = index
        maxvalue = max(maxvalue,pArray[index])
    print mArray
    print pArray
    return maxvalue-1 if maxvalue>0 else 0
#print mancher("kabcbadabcbaz")
print mancher("abc12321")