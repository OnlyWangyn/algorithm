class Solution(object):
    def topKFrequent(self, nums, k):
        data={}
        for n in nums:
            data[n]=data[n]+1 if n in data else 1
        bucket=[[] for i in xrange(len(nums)+1)]
        for key in data:
            bucket[data[key]].append(key)
        result=[]
        for i in xrange(len(bucket)-1,-1,-1):
            if len(result)<k:
                result.extend(bucket[i])
            else:
                break
        return result
s = Solution()
print s.topKFrequent([1,1,1,1,1,1],2)