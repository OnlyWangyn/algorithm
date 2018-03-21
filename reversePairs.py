class Solution:
    """
    @param: A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        if len(A) == 0:
            return 0
        return self.mergeSort(A,0,len(A)-1)
    def mergeSort(self,A,left,right):
        if right == left:
            return 0
        mid = left+(right - left)/2
        rightnum = self.mergeSort(A,left,mid)
        leftnum=self.mergeSort(A,mid+1,right)
        final = self.merge(A,left,mid,right)
        return rightnum+leftnum+final
    def merge(self,A,left,mid,right):
        p1 = left
        p2 = mid+1
        help = [ 0 for i in range(right - left + 1)]
        index = 0
        num =0
        while p1<=mid and p2<=right:
            if A[p1]<=A[p2]:
                help[index] = A[p1]
                index+=1
                p1+=1
            else:
                help[index]=A[p2]
                num += mid - p1+1
                index+=1
                p2+=1
        while p1<=mid:
            help[index] = A[p1]
            index+=1
            p1+=1
        while p2<=right:
            help[index] = A[p2]
            index+=1
            p2+=1
        for i in range(len(help)):
            A[left+i] = help[i]
        return num
solution = Solution()
print solution.reversePairs([4,3,2,1])