import random
def main(array,k):
    length = len(array)
    if(length<2):
        return
    res = select(array, 0,len(array)-1, k - 1)
    print res

def select(array, left, right, k):
    if(left==right):
        return array[left]
    mid = medianOfMedians(array,left,right)
    range=partition(array,left,right,mid)
    if k>=range[0] and k<=range[1]:
        return array[k]
    elif k < range[0]:
        return select(array, left, range[0] - 1, k)
    else:
        return select(array, range[1] + 1, right, k)

def medianOfMedians(array,left,right):
    num = right - left + 1
    offset = 0 if num % 5 == 0 else 1
    arr=[0 for i in range(num/5+offset)]
    for i in range(len(arr)):
        leftI = left+i*5
        rightI = leftI+4
        arr[i]= getMedian(array,leftI,min(rightI,right))
    return select(arr,0,len(arr)-1,len(arr)/2)

def getMedian(array,left,right):
    insertSort(array,left,right)
    sum = left+right
    return array[sum/2+sum%2]

def insertSort(array,left,right):
    i = left+1
    while i<right:
        j=i-1
        while j>=0 and array[j]>array[j+1]:
            swap(array,j,j+1)
            j-=1
        i+=1

def partition(array,left,right,mid):
    less = left - 1
    more = right
    while left < more:
        if array[left]<mid:
            less+=1
            swap(array,less, left)
            left+=1
        elif array[left]>mid:
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