# .四数之和
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。
# 示例 1：

# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 示例 2：

# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  

# 提示：

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()# 排序
        res = []# 初始化res
        for i in range(len(nums) - 3):# 循环遍历
            if i > 0 and nums[i] == nums[i - 1]:# 如果i不等于0且nums[i]等于nums[i-1]
                continue# 跳过
            for j in range(i + 1, len(nums) - 2):# 循环遍历
                if j > i + 1 and nums[j] == nums[j - 1]:# 如果j不等于i+1且nums[j]等于nums[j-1]
                    continue# 跳过
                k, l = j + 1, len(nums) - 1# k和l初始化
                while k < l:# 循环遍历
                    sum = nums[i] + nums[j] + nums[k] + nums[l]# 初始化sum
                    if sum == target:# 如果sum等于target
                        res.append([nums[i], nums[j], nums[k], nums[l]])# 将nums[i], nums[j], nums[k], nums[l]加入res
                        k += 1# k加1
                        l -= 1# l减1
                        while k < l and nums[k] == nums[k - 1]:# 如果k不等于l且nums[k]等于nums[k-1]
                            k += 1# k加1
                        while k < l and nums[l] == nums[l + 1]:# 如果k不等于l且nums[l]等于nums[l+1]
                            l -= 1# l减1
                    elif sum < target:# 如果sum小于target
                        k += 1# k加1
                    else:# 否则
                        l -= 1# l减1
        return res

def test1():
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0))

    

test1()