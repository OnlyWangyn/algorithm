import numpy as np

def group_consecutive(nums):
    result = []
    temp = []
    size = len(nums)
    for index in range(size - 1):
        temp.append(nums[index])
        if nums[index + 1] != nums[index]+1:
            result.append(temp)
            temp = []
    if (len(temp)>0):
        result.append(temp)
    return result
def grouo1(nums):
    return np.split(nums,(np.where(np.diff(nums)!=1))[0]+1)
a =  [1, 2, 3, 7, 8, 9, 10, 100, 101, 102, 103]
d = np.diff(a)
print d
print np.where(d!=1)[0]+1
print group_consecutive(a)

