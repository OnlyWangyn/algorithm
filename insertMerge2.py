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
        start=newInterval[0]
        end=newInterval[1]
        size=len(intervals)
        result=[]
        if(size==0):
            result.append([start,end])
            return result
        for index in range(size):
            inter = intervals[index]
            if start > inter[1]:
               result.append(inter)
            if end < inter[0]:
                result.append(newInterval)
                k = index
                while k < size:
                    result.append(intervals[k])
                    k+=1
                break
            if start<=intervals[index][1] and end >=intervals[index][0]:
                start = min(start,intervals[index][0])
                end = max(end,intervals[index][1])
            if index == size -1:
                result.append([start,end])
        print result
solu = Solution()
solu.insert([[1,5],[7,8],[10,13]],[6,7])
