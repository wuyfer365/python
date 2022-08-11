#不同路径
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

# 问总共有多少条不同的路径？

# 示例 1：


# 输入：m = 3, n = 7
# 输出：28
# 示例 2：

# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
# 示例 3：

# 输入：m = 7, n = 3
# 输出：28
# 示例 4：

# 输入：m = 3, n = 3
# 输出：6

# 提示：

# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10^9
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for i in range(n)] for j in range(m)]#初始化一个二维数组 每个元素都是1
        for i in range(1, m):#从第二行开始
            for j in range(1, n):#从第二列开始
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]#返回最后一行最后一列的值

def test1():
    m = 3
    n = 7
    s = Solution()
    print(s.uniquePaths(m, n))
test1()
