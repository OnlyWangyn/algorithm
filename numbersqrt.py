#coding:utf-8
"""
给定一个正整数（int类型），判断这个整数是否是某个数的平方。

注意：不允许使用任何内置函数如sqrt直接计算。


算法分析

这道题的题目描述很简单，和另一道题（求一个整数的平方根）类似。刷题君的思路是用二分答案法。

二分答案法的前提是答案需要具有单调性。对于这道题而言，单调性体现在答案左边的数，平方都小于给定的正整数；答案右边的数，平方都大于给定的正整数。

考虑到给定的正整数是int类型，最大是2的31次方，大约是2.1*10^9，那么二分的边界最大不超过50000。这个算法的时间复杂度是O(log min(50000, num))。

当然本题还有很多其他的方法，比如用牛顿法逼近，比如用累加的方法（任何平方数均可以表示为1+3+5+7+...），这两种方法的时间复杂度是O(sqrt(num))。

因为无法使用任何内置函数，本题没有O(1)时间复杂度的做法，最好的做法就是log级别的，通过缩小二分的范围可以提升算法的效率。

"""
def isPerfectSqrt(num):
    mid = num/2
    while mid>=0:
        if mid * mid>num:
            mid = mid/2
        elif mid * mid == num:
            return True
        elif mid * mid < num:
            return False
    return True

def isPerfectSqrt2(num):
    left = 0
    right =min(50000,num)
    while(left<=right):
        mid = left+(right-left)/2
        if mid * mid == num:
            return True
        if mid * mid < num:
            left=mid+1
        else:
            right = mid -1
    return False
print isPerfectSqrt2(1)