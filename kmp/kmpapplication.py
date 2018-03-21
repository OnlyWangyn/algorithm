#coding=utf-8 题眼两个字符串贴在一起求最大前缀和后缀匹配,最大前缀和后缀能重多少不重的部分贴在后面
def getLastNext(str):
    if(len(str)==1):
        return -1
    strlist=list(str)
    strlist.append("")
    next=[0 for i in range(len(strlist))]
    next[0]=-1
    next[1]=0
    index=2
    current=0
    while index < len(strlist):
        if strlist[index-1]==strlist[current]:
            current+=1
            next[index]=current
            index+=1
        elif current>0:
            current=next[current]
        else:
            next[index]=0
            index+=1
    return next[len(next)-1]
def getSmallestDoubleSelf(str):
    prefixLength= getLastNext(str)
    if prefixLength ==-1 or prefixLength==0:
        return str+str
    length = len(str)
    if length % prefixLength !=0:
        index =prefixLength- (length - prefixLength)
        prefixLength =index+ len(str) % prefixLength
    else:
        index=0
    strlist = list(str)
    while index < prefixLength:
        strlist.append(strlist[index])
        index+=1
    return "".join(strlist)
print getSmallestDoubleSelf("abcabcab")
print getSmallestDoubleSelf("aaa")