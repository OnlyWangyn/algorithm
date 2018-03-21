import heapq
import costandprofitNode
class PriorityQueue:
    def __init__(self):
        self.data=[]
    def push(self,item,priority):
        heapq.heappush(self.data,(-priority,item))
    def pop(self):
        return heapq.heappop(self.data)
    def isEmpty(self):
        return True if len(self.data) ==0 else False
    def peek(self):
        return self.data[0]
#test case
# node1 = costandprofitNode.Node(2,20)
# node2 = costandprofitNode.Node(1,30)
# heap = PriorityQueue()
# heap.push(node1,node1.profit)
# heap.push(node2,node2.profit)
# print heap.data
# while not heap.isEmpty():
#     n = heap.pop()
#     print n[1].cost
