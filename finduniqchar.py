def firstUniqChar(s):
    length = len(s)
    records={}
    for i in range(0,length):
        if s[i] not in records.keys():
            records[s[i]] = 1
        else:
            records[s[i]] += i
    for value in s:
        if(records[value]==1):
            return s.index(value)
    return -1
print firstUniqChar("lovelintcode")