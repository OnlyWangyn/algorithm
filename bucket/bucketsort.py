import sys
def bucketSort(array):
    if len(array)<2:
        return array
    bucket= {}
    for a in array:
        if a not in bucket.keys():
            bucket[a]=1
        else:
            bucket[a]+=1
    position = 0
    for index in bucket.keys():
        while bucket[index]>0:
            array[position]=index
            bucket[index]-=1
            position+=1
    return array
array=[1,5,2,6,7,0]
print bucketSort(array)
