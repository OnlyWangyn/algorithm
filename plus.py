def add(a,b):
    carry = 1
    while(carry!=0):
        s = a ^ b
        print s
        carry =( a & b)<<1
        a = s
        b = carry
    return a
def recusive(a,b):
    if(b==0):
        print a
        return
    s =  a ^ b
    c =( a & b)<<1
    recusive(s,c)
recusive(2,3)