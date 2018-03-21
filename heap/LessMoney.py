import MinHeap
def lessMoney(array):
    heap = MinHeap.MinHeap()
    for x in array:
        heap.push(x)
    sum=0
    while heap.size()>1:
        poll = heap.pop()+heap.pop()
        sum+=poll
        heap.push(poll)
    return sum
testcase1 = [10,20,30]
testcase2 = [ 6, 7, 8, 9 ]
print lessMoney(testcase1)
print lessMoney(testcase2)

