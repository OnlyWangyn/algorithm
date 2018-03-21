
def anagram(s,t):
    a = sorted(s)
    b = sorted(t)
    return a == b
def anagram1(s, t):
    sList = list(s)
    tList = list(t)
    stillOK = True
    pos0 = 0;
    while pos0 < len(sList) and stillOK:
        pos1 = 0
        found = False
        while pos1 < len(tList) and not found:
            if(sList[pos0] == tList[pos1]):
                found = True
            else:
                pos1=pos1+1
        if(found):
            tList[pos1] = None
        else:
            stillOK = False
        pos0 = pos0 + 1
    return stillOK
print anagram1("aacc","ccac")