import random
def main(array):
    length = len(array)
    if(length<2):
        return
    quicksort(array,0,len(array)-1)
    print array
def quicksort(array,left,right):
    if(left>=right):
        return
    mid = left+(right - left +1)*random.randrange(0,1)
    swap(array,mid,right)
    range=partition(array,left,right)
    quicksort(array,left,range[0])
    quicksort(array,range[1],right)
def partition(array,left,right):
    less = left - 1
    more = right
    while left < more:
        if array[left]<array[right]:
            less+=1
            swap(array,less, left)
            left+=1
        elif array[left]>array[right]:
            more-=1
            swap(array,left, more)
        else:
            left+=1
    swap(array,more, right)
    return [less,more+1]
def swap(array,i, j):
    if i==j:
        return
    array[i]= array[i]^array[j]
    array[j]= array[i]^array[j]
    array[i]=array[i]^array[j]
a = [0,9,2,8,3,7,4,6,5,1]
main(a)