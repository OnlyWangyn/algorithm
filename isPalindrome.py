class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        right = 0
        left = len(s)-1
        while(right<left):
            if (not s[right].isalpha()) and (not s[right].isdigit()):
                right+=1
                continue
            if (not s[left].isalpha()) and (not s[left].isdigit()):
                left-=1
                continue
            if s[right].lower() == s[left].lower():
                right+=1
                left-=1
            else:
                return False
        return True
solution = Solution()
print solution.isPalindrome("race a car")


