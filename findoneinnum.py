def countOnes(num):
    count = 0
    flag = 1
    while num & flag:
        count +=1
        flag= flag<<1
    return count
print countOnes(32)