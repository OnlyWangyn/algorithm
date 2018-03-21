class Solution:
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
interval=[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
solution = Solution()
solution.merge(interval)