import random
def main(array,k):
    length = len(array)
    if(length<2):
        return
    res = quicksort(array,0,len(array)-1,k-1)
    print array
    print res
def quicksort(array,left,right,k):
    if(left==right):
        return array[left]
    mid = left+int((right - left +1)*random.random())
    swap(array,mid,right)
    range=partition(array,left,right)
    if k>=range[0] and k<=range[1]:
        return array[k]
    elif k < range[0]:
        return quicksort(array,left,range[0]-1,k)
    else:
        return quicksort(array,range[1]+1,right,k)

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
    return [less+1,more]
def swap(array,i, j):
    if i==j:
        return
    array[i]= array[i]^array[j]
    array[j]= array[i]^array[j]
    array[i]=array[i]^array[j]
a = [0,9,2,8,3,7,4,6,5,1]
main(a,2)