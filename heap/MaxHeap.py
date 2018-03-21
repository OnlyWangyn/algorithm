#encoding=utf-8
import heapq
class MaxHeap(object):
    def __init__(self):
        self.data=[]
    def push(self,value):
        value = -value
        heapq.heappush(self.data,value)
    def pop(self):
        value = heapq.heappop(self.data)
        return -value
    def peek(self):
        value = self.data[0]
        return -value
    def size(self):
        return len(self.data)
    def printHead(self):
        print [-x for x in self.data]
# x = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# m = MaxHeap()
# m.push(1)
# m.push(8)
# m.push(2)
# m.push(23)
# m.push(7)
# m.push(4)
# m.printHead()
