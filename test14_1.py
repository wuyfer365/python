#最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。
# 提示：

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
# 输入：["flower","flow","flight"]
# 输出："fl"
# 输入：["dog","racecar","car"]
# 输出：""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        strs_len=len(strs)
        strs_min_len=len(strs[0])
        curr=0
        for i in range(1,strs_len):
            if len(strs[i])<strs_min_len:
                strs_min_len=len(strs[i])
                curr=i

        for i in range(strs_min_len):# 循环遍历列表中的每一个字符串
            for j in range(1,strs_len):# 循环列表中除了第一个字符串的其他字符串
                if strs[0][i]!=strs[j][i]:# 如果第一个字符串的第i个字符与其他字符串的第i个字符不相等
                    return strs[0][:i]# 则返回第一个字符串的前i个字符
        return strs[curr]# 如果循环结束，则返回第一个字符串
def test1():
    s=Solution()
    print(s.longestCommonPrefix(["ab", "a"]))
    # print(s.convert("PAYPALISHIRING",4))
    
test1()