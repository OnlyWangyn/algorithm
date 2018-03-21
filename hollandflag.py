def main(array):
    length=len(array)
    sort(array,0,length-1)
    print array
def sort(array,left,right):
    if(left>=right):
        return
    partition(array,left,right)
def partition(array,current,right):
    less = current-1
    while current < right:
        if array[current]=="red":
            less+=1
            swap(array,less,current)
            current+=1
        elif array[current]=='blue':
            swap(array,current,right)
            right-=1
        elif array[current] == "white":
            current+=1
def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j]=temp
array=['red','white','red','blue','blue','white','red','blue']
main(array)