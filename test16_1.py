# 最接近的三数之和
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

# 返回这三个数的和。
# 假定每组输入只存在恰好一个解。
# 示例 1：

# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 示例 2：

# 输入：nums = [0,0,0], target = 1
# 输出：0
# 提示：

# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()# 排序
        res = nums[0] + nums[1] + nums[2]# 初始化res
        for i in range(len(nums) - 2):# 循环遍历
            j, k = i + 1, len(nums) - 1# j和k初始化
            while j < k:# j和k循环
                sum = nums[i] + nums[j] + nums[k]# 和
                if sum == target:# 如果和等于target
                    return sum# 返回和
                if abs(sum - target) < abs(res - target):# 如果和与target的差值小于res与target的差值
                    res = sum# 更新res
                if sum < target:# 如果和小于target
                    j += 1# j加1
                elif sum > target:# 如果和大于target
                    k -= 1# k减1
        return res