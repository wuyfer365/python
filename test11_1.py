# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 返回容器可以储存的最大水量。

# 说明：你不能倾斜容器。

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #暴力解法，每次都从两头向中间找，找到最大的面积
        #每次找到的面积都是两条线的长度乘以两条线的最小高度
        #时间复杂度O(n^2)
        #空间复杂度O(1)
        # if len(height)<2:
        #     return 0
        # max_area=0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         area=min(height[i],height[j])*(j-i)
        #         if area>max_area:
        #             max_area=area
        # return max_area
        #改进的暴力解法，从两头向中间找，找到最大的面积
        #时间复杂度O(n)
        #空间复杂度O(1)
        if len(height)<2:
            return 0
        max_area=0
        left=0
        right=len(height)-1
        while left<right:
            area=min(height[left],height[right])*(right-left)
            if area>max_area:
                max_area=area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
        