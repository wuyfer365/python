# 给定一个整数数组和一个整数k，找出数组中和为k的两个数。
# 并返回他们的数组下标。

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, num in enumerate(nums):
        if num in d:
            return [d[num], i]
        else:
            d[target - num] = i
    return []


# 测试twoSumpy
def test1():
    nums = [2, 7, 11, 15]
    target = 9
    assert twoSum(nums, target) == [0, 1]

