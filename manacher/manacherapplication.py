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
def mancherapplication(str):
    if len(str)<1:
        return 0
    mArray = manacherString(str)
    r = -1
    c = -1
    maxcontainedEnd= -1
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
        if (r == len(mArray)):
            maxcontainedEnd = pArray[index]
            break
    needLength = len(str)-maxcontainedEnd + 1
    res = [0 for i in range(needLength)]
    for index in range(needLength):
        res[needLength-index-1] = mArray[2*index+1]
    print res
    # dict =2*c-r
    # res=list(str)
    # for i in range(dict,-1,-1):
    #     if mArray[i]!="#":
    #         res.append(mArray[i])
    # print res

#print mancherapplication("kabcbadabcba")
# print mancherapplication("abc12321")
#print mancherapplication("abc12321z")
print mancherapplication("abcd123321")