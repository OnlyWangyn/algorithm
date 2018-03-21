# @return {int} the number you guess
def guess(target):
    if target < 4:
        return 1
    if target > 4:
        return -1
    else:
        return 0
def guessNumber(n):
    low = 1
    high =n
    while low < high:
        mid = (low+high)/2
        guessResult = guess(mid)
        if guessResult == 1:
            high=mid-1
        elif guessResult == -1:
            low = mid +1
        else:
            return mid
    return low
def guessNumber1(n):
    L, R = 1, n
    while L <= R:
        mid= L + ((R - L) >> 1)
        res = guess(mid)
        if res == 0:
            return mid
        elif res == 1:
            L = mid + 1
        else:
            R = mid - 1
    return L
print guessNumber1(10)
