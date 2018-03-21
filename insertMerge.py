"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        result=[]
        size = len(intervals)
        index = 0
        while index < size:
            if newInterval[0]> intervals[index][0] and newInterval[1] > intervals[index][1]:
                result.append(intervals[index])
            if newInterval[0] < intervals[index][0] and newInterval[1] < intervals[index][1]:
                result.append(newInterval)
                break
            index+=1
        while index < size:
            result.append(intervals[index])
            index+=1
        return self.merge(result)
    def merge(self,interval):
        result = []
        size = len(interval)
        i=0
        interval.sort(key=lambda d: d[0])
        print interval
        while i < size:
            block = interval[i]
            left = block[0]
            right = block[1]
            k = i+1
            while k < size:
                b2 = interval[k]
                if(b2[0]<= right):
                    right = max(right,b2[1])
                    k+=1
                else:
                    break
            temp=[left,right]
            result.append(temp)
            i=k
        print result
solution = Solution()
print solution.insert([[1,2], [5,9]],[3,4])
