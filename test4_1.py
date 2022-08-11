#给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#算法的时间复杂度应该为 O(log (m+n)) 。

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==0:
            return (nums1[len(nums1)/2]+nums1[len(nums1)/2-1])/2.0
        else:
            return nums1[len(nums1)/2]