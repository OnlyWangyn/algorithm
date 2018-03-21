#encoding=utf-8
#取得中位数
import MaxHeap
import MinHeap
class MedianHolder:
    def __init__(self):
        self.maxHeap = MaxHeap.MaxHeap()
        self.minHeap= MinHeap.MinHeap()
    def modifyTwoHeapSize(self):
        maxSize = self.maxHeap.size()
        minSize = self.minHeap.size()
        if maxSize == minSize+2:
            self.minHeap.push(self.maxHeap.pop())
        elif minSize == maxSize+2:
            self.maxHeap.push(self.minHeap.pop())
    def addNum(self,num):
        if self.maxHeap.size()==0 or self.maxHeap.peek()>=num:
            self.maxHeap.push(num)
        else:
            self.minHeap.push(num)
        self.modifyTwoHeapSize()
    def getMedian(self):
        maxSize = self.maxHeap.size()
        minSize = self.minHeap.size()
        if maxSize == 0 or minSize ==0:
            return None
        maxPeek = self.maxHeap.peek()
        minPeek = self.minHeap.peek()
        if (maxSize + minSize)%2 ==0:
            return (maxPeek+minPeek)/2
        return maxPeek if maxSize>minSize else minPeek
# test case  1  偶数个
array = [21,0,2,17,1,28]
mh = MedianHolder()
for x in array:
    mh.addNum(x)
print mh.getMedian()
array2 = sorted(array)
mid = len(array2)/2
median = (array[mid-1]+array[mid])/2
print median
#test case 2   奇数个
array = [21,0,2,1,28]
mh = MedianHolder()
for x in array:
    mh.addNum(x)
print mh.getMedian()
array2 = sorted(array)
mid = len(array2)/2
median = array[mid]
print median