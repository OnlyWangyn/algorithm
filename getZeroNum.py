def getZeroNum(num):
    if num == 0 :
        return 0
    res = 1
    for n in range(num,0,-1):
        res *= n
    count =0
    while res % 10 == 0:
        res/=10
        count+=1
    return count
print getZeroNum(1)