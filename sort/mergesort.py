def mergesort(array):
    if len(array) == 0:
        return array
    result= partition(array,0,len(array)-1)
    print result
def partition(array,left,right):
    if left == right:
        return 0
    mid = left+(right - left)/2
    a = partition(array,left,mid)
    b = partition(array,mid+1,right)
    c =merge(array,left,mid,right)
    print c
    return a +b +c

def merge(array,left,mid,right):
    res = 0
    help = [ 0 for i in range(right - left + 1)]
    p1 = left
    p2 = mid+1
    index = 0
    while p1<=mid and p2 <= right:
         if array[p1]< array[p2]:
             help[index] = array[p1]
             res = array[p1]*(right-p2+1)
             p1+=1
         else :
             help[index] = array[p2]
             p2+=1
         index+=1
    while p1<=mid:
        help[index] = array[p1]
        index+=1
        p1+=1
    while p2<=right:
        help[index] = array[p2]
        index+=1
        p2+=1
    for i in range(len(help)):
        array[left+i] = help[i]
    return res
a = [0,9,2,8,3,7,4,6,5,1]
mergesort(a)