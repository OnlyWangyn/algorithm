#!/usr/bin/python
# coding:utf-8
from collections import Counter
def findAnagrams(s,p):
    index=[]
    c = Counter(p)#字典cp记录要凑成目标字符串p的anagram，各字符分别缺多少个
    lp = len(p)
    count  = lp#整数count记录凑成目标字符串p一共还缺多少个字符
    for i in range(len(s)):
        sub = s[i]
        if(c[sub] >=1):
            count -=1
        c[sub] -=1
        if i >= lp:
            if c[s[i-lp]] >= 0:
                count +=1
            c[s[i-lp]]+=1
        if(count == 0):
            index.append(i - len(p)+1)
    return index
print findAnagrams('abab','ab')
