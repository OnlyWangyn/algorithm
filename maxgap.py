class Solution:
    """
    @param: nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        if(len(nums)<2):
            return 0
        maxNum=-float('inf')
        minNum=float('inf')
        for n in nums:
            maxNum =max(maxNum,n)
            minNum = min(minNum,n)
        if maxNum == minNum:
            return 0
        length = len(nums)
        hasNum = [False for i in range(length+1)]
        minArray=[0 for i in range(length+1)]
        maxArray=[0 for i in range(length+1)]
        for n in nums:
            bid = self.bucket(n,minNum,maxNum,length)
            minArray[bid] = min(minArray[bid],n) if hasNum[bid] else n
            maxArray[bid] = max(maxArray[bid],n) if hasNum[bid] else n
            hasNum[bid] = True
        lasMax = maxArray[0]
        res=0
        index = 1
        while index < len(hasNum):
            if hasNum[index]:
                res = max(res,minArray[index]-lasMax)
                lasMax =maxArray[index]
            index+=1
        return res
    def bucket(self,num,min,max,len):
        return (num-min)*len/(max - min)
s = Solution()
print s.maximumGap([999,999,999])