class Solution:
    """
    @param: digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        left = len(digits)-1
        while left>=0:
            if digits[left]+1<10:
                digits[left]=digits[left]+1
                break
            else:
                digits[left]=0
                left-=1
        if left < 0:
            digits.insert(0,1)
        return digits
solution = Solution()
print solution.plusOne([9,9,9])