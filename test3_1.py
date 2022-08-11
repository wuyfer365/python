# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例 1:
# 输入: "abcabcbb"
# 输出: 3   
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 输入: "aab"
# 输出: 2
# 解释: 因为无重复字符的最长子串是 "aa"，所以其长度为 2。

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        max_length=1
        start=0
        end=1
        while end<len(s):# 循环遍历字符串
            if s[end] not in s[start:end]:# 如果不存在重复字符，则继续向后查找
                end+=1# 向后查找
            else:
                start=s.index(s[end],start)+1# 如果在start到end中有重复的字符，则start设置为重复字符的下一个位置
                end=start+1# end设置为重复字符的下一个位置
            if end-start>max_length:# 如果当前的最长子串比之前的最长子串长，则更新最长子串的长度
                max_length=end-start# 更新最长子串的长度
        return max_length

# 测试twoSumpy
def test1():
    nums = "abcabcbb"
    assert Solution().lengthOfLongestSubstring(nums) == 3