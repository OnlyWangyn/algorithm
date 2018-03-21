def stringpermutation(A,B):
    # i = 0
    # a = list(A)
    # b = list(B)
    # if len(a)!= len(b) or A == '' and B !='' or A!='' and B == '':
    #     return False
    # while i < len(a):
    #     currA = a[i]
    #     j = 0
    #     while j < len(b):
    #         if(currA == b[j]):
    #             b[j] = None
    #             break
    #         j = j+1
    #     if(j== len(b)):
    #         return False
    #     i = i+1
    # return True
    if A == None and B ==None:
        return True
    if len(A)!= len(B):
        return False
    result = {}
    for i in range(0,len(A)):
        if A[i] not in result.keys():
            result[A[i]] = 1
        else:
            result[A[i]] +=1
        if B[i] not in result.keys():
            result[B[i]] = -1
        else:
            result[B[i]] -=1
    for key in result:
        if result[key]!=0:
            return False
    return True



print stringpermutation('abcd','bcad')

