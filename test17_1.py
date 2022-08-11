# 电话号码的字母组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 2 -> abc, 3 -> def,4 -> ghi,5 -> jkl,6 -> mno,7 -> pqrs,8 -> tuv,9 -> wxyz

# 示例 1：

# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 示例 2：

# 输入：digits = ""
# 输出：[]
# 示例 3：

# 输入：digits = "2"
# 输出：["a","b","c"]

# 提示：

# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        self.dfs(digits, 0, '', res, dict)# 调用dfs函数
        return res

    def dfs(self, digits, index, path, res, dict):# 回溯法 递归 深度优先搜索 
        """
        :type digits: str# 当前的字符串
        :type index: int# 当前的下标
        :type path: str# 当前的路径
        :type res: List[str]# 结果
        :type dict: dict# 字典
        :rtype: None# 无返回值
        功能描述：
        """
        if index == len(digits):# 如果下标等于字符串长度
            res.append(path)# 将路径添加到结果中
            return# 结束递归
        for i in dict[digits[index]]:# 循环当前字符串的字符
            self.dfs(digits, index + 1, path + i, res, dict)# 递归 当前字符串的字符 和 当前路径 和 结果 和 字典 

def test1():
    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits))

test1()