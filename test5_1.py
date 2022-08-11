#给你一个字符串 s，找到 s 中最长的回文子串。如果存在多个长度相等的回文子串，只需返回其中一个。
#输入：s = "babad"
#输出："bab"
#注意: "aba" 也是一个有效答案。

#输入：s = "cbbd"
#输出："bb"
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        max_len=1
        start=0
        for i in range(len(s)):# 循环遍历字符串
            if i-max_len>=1 and s[i-max_len-1:i+1]==s[i-max_len-1:i+1][::-1]:# 如果当前的回文子串是回文串，则更新最长回文子串的长度
                start=i-max_len-1# 更新最长回文子串的起始位置
                max_len+=2# 更新最长回文子串的长度
                continue# 跳出当前循环
            if i-max_len>=0 and s[i-max_len:i+1]==s[i-max_len:i+1][::-1]:# 如果当前的回文子串是回文串，则更新最长回文子串的长度
                start=i-max_len
                max_len+=1
        return s[start:start+max_len]
        
        