from costandprofitNode import Node
import MinHeap
import PriorityQueue
def getMaxProfit(costs,profits,c,k):
    if len(costs)!=len(profits):
        return 0
    data=[]
    for i in range(len(costs)):
        node = Node(costs[i],profits[i])
        data.append(node)
    costMinHeap = MinHeap.MinHeap()
    for d in data:
        costMinHeap.push(d)
    profitsMaxHeap = PriorityQueue.PriorityQueue()
    for index in range(k):
        while not costMinHeap.isEmpty() and costMinHeap.peek().cost <=c:
            n = costMinHeap.pop()
            profitsMaxHeap.push(n,n.profit)
        if profitsMaxHeap.isEmpty():
            break
        item = profitsMaxHeap.pop()
        c +=item[1].profit
    return c
costs=[10,20,30]
profits=[10,10,20]
print getMaxProfit(costs,profits,10,3)