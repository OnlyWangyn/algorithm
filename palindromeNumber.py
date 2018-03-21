def palindromeNumber(num):
    numstr = str(num)
    mid = len(numstr)/2
    for index in range(0,mid):
        start = numstr[index]
        end = numstr[len(numstr)-1-index]
        if end!=start:
            return False
    return True
print palindromeNumber(12321)