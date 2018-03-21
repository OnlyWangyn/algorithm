def isValidParentheses(s):
    size = len(s)
    if size == 0:return False
    findPair = False
    limit = size
    for index in range(size):
        j = index
        pairIndex = -1
        while j < limit:
            if isPair(s[index],s[j]):
                findPair = True if (j-index-1) % 2 == 0 or (j-index-1)==0 else False
                pairIndex = j
            j=j+1
        if(pairIndex!=-1):
            limit = pairIndex
        elif pairIndex == -1:
            return False
        if(j == limit):
            limit = size
    return findPair
def isPair(a,b):
    flag1 = a == "(" and b == ")"
    flag2= a=="[" and b == "]"
    flag3 = a =="{" and b == "}"
    return flag1 or flag2 or flag3
print isValidParentheses("()")

#[([]])
#([)]



