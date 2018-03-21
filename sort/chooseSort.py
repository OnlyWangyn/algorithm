def chooseSort(array):
    if len(array) < 2:
        return array
    for index in range(0,len(array)):
        minIndex = index
        for j in range(index+1,len(array)):
            if array[j]<array[minIndex]:
                minIndex = j
        swap(array,index,minIndex)
    return array
def swap(array,i, j):
    if i==j:
        return
    array[i]= array[i]^array[j]
    array[j]= array[i]^array[j]
    array[i]=array[i]^array[j]
originArray = [1,7,3,89,12,100]
print chooseSort(originArray)