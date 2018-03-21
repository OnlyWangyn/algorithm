def smallerEqualBiggerForArray(array,pivot):
    if len(array)==0:
        return
    start =0
    small=-1
    end = len(array)-1
    while start<= end:
        if array[start]>pivot:
            temp=array[start]
            array[start]=array[end]
            array[end]=temp
            end-=1
        elif array[start]<pivot:
            small+=1
            temp=array[small]
            array[small]=array[start]
            array[start]=temp
            start+=1
        elif array[start]== pivot:
            start+=1
    return array
array=[7,2,3,4,1,2,3,8,9,0]
#array=[2,7,8,9]
print smallerEqualBiggerForArray(array,3)

