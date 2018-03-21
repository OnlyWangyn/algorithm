import heapq
import costandprofitNode
class MinHeap:
    def __init__(self):
        self.data=[]
    def push(self,value):
        heapq.heappush(self.data,value)
    def pop(self):
        return heapq.heappop(self.data)
    def printHeap(self):
        print [x for x in self.data]
    def peek(self):
        value = self.data[0]
        return value
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return True if len(self.data)==0 else False

#Test case
# node1 = costandprofitNode.Node(2,20)
# node2 = costandprofitNode.Node(1,30)
# heap = MinHeap()
# heap.push(node1)
# heap.push(node2)
# while not heap.isEmpty():
#     n = heap.pop()
#     print n.cost
#     print n.profit