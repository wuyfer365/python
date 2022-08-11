# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#提示：
# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s 只包含从 a-z 的小写字母。
# p 只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #python3中的正则表达式全匹配
        import re
        p="^"+p+"$"
        return re.match(p,s) is not None   #这里的is not None是为了防止re.match(p,s)为None
def test1():
    s=Solution()
    print(s.isMatch("aa","a."))

test1()   