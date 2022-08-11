#三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
# 输入：nums = []
# 输出：[]
# 示例 3：
# 输入：nums = [0]
# 输出：[]
# 提示：
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()# 先排序
        res=[]# 创建结果列表
        for i in range(len(nums)-2):# 循环遍历列表中的每一个数字
            if i>0 and nums[i]==nums[i-1]:# 如果当前数字与上一个数字相同，则跳过
                continue        
            l,r=i+1,len(nums)-1# 分别设置左右指针
            while l<r:# 如果左指针小于右指针
                s=nums[i]+nums[l]+nums[r]# 计算和
                if s<0:# 如果和小于0
                    l+=1# 左指针右移
                elif s>0:# 如果和大于0
                    r-=1# 右指针左移
                else:# 如果和等于0
                    res.append([nums[i],nums[l],nums[r]])# 将结果添加到结果列表
                    while l<r and nums[l]==nums[l+1]:# 如果左指针与左指针的下一个数字相同，则左指针右移
                        l+=1
                    while l<r and nums[r]==nums[r-1]:# 如果右指针与右指针的上一个数字相同，则右指针左移
                        r-=1
                    l+=1# 左指针右移
                    r-=1# 右指针左移
        return res