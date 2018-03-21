def isHappy(n):
    while n !=1 and n!=4:
        newNum = 0
        while n > 0:
            m=n % 10
            newNum += m * m
            n= n/10
        n = newNum
    if n == 1:
        return True
    if n == 4:
        return False
    return True
#print isHappy(2)
def isUgly(num):
    pf = [2,3,5]
    while num > 0:
        i = 0
        while i < len(pf):
            mod = num % pf[i]
            if mod == 0:
                num = num /pf[i]
                break
            i+=1
        if i == 3:
            return False
        if num == 1:
            return True
    return True
print isUgly(14)

