# class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    # def longestPalindrome(self,s):
    #     max=0
    #     size = len(s)
    #     for i in range(0,size):
    #         for j in range(0,size):
    #             result = self.isPalindrome(s,i,j)
    #             if result:
    #                 curLen = j-i+1
    #                 max = curLen if curLen > max else max
    #     return max
    #
    # def isPalindrome(self,s,start,end):
    #     while start < end and end < len(s):
    #         startstr = s[start]
    #         endstr = s[end]
    #         if startstr != endstr:
    #             return False
    #         start+=1
    #         end-=1
    #     return True
def longestPalindrome(s):
    count = {}
    max = 0
    hasOdd = False
    for str in s:
        if str not in count.keys():
            count[str] = 1
        else:
            count[str] +=1
    if len(count) == 1:
        return count.values()
    for value in count:
        if count[value]%2 == 0:
            max +=count[value]
        else:
            hasOdd = True
            max +=count[value]-1
    return max + 1 if hasOdd else max


print longestPalindrome('NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy')
