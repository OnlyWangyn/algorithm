class Solution():
    def reverseVowels(self,s):
        start = 0
        end = len(s) -1
        sIndex =-1
        eIndex = -1
        array =[ x for x in s]
        while start<=end:
            if self.isVowel(s[start]):
                while start<=end:
                    if self.isVowel(s[end]):
                        array[start] ,array[end] = array[end],array[start]
                        end-=1
                        break
                    end-=1
            start+=1

        return "".join(array)
    def isVowel(self,c):
        vowel = ['a','e','i','o','u']
        return False if c.lower() not in vowel else True
s = Solution()
print s.reverseVowels("aA")