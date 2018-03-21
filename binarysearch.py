def binarySearch(nums,target):
    low = 0
    high = len(nums) -1
    current = -1
    while(low < high):
        mid = (low+high)/2
        midv = nums[mid]
        if target<midv:
            high=mid -1
        elif target>midv:
            low = mid +1
        else:
            current = mid
            high= mid-1
    if target == nums[low]:
        current = low
    return current
print binarySearch([2,6,8,13,15,17,17,18,19,20],15)

