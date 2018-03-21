import heapq
def heapsort(array):
    h=[]
    for x in array:
        heapq.heappush(h,x)
    print [heapq.heappop(h) for i in range(len(h)) ]
array=[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapsort(array)