def heapsort(array):
    if len(array)<2:
        return
    for index in range(0,len(array)):
        heapinsert(array,index)
    size = len(array)-1
    swap(array,0,size)
    while size > 0:
        heavyify(array,0,size)
        size =size-1
        swap(array,0,size)
    return array
def heapinsert(array,index):
    while index-1>=0 and (array[index]>array[(index-1)/2]):
        swap(array,index,(index-1)/2)
        index = (index-1)/2
def heavyify(array,index,size):
    left = index*2 +1
    while left  < size:# left >= size means no child
        largest = (left+1) if (left+1<size) and array[left+1]>array[left] else left
        if array[largest] < array[index]:
            break
        swap(array,largest,index)
        index = largest
        left = index*2 + 1

def swap(array,i,j):
    if i==j:
        return
    array[i]=array[i]^array[j]
    array[j]=array[i]^array[j]
    array[i]=array[i]^array[j]
print heapsort([-42, 2 ,-2 ,29, -30, 49, -16, 55, 24, 15])