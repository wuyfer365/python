#给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
#假设环境不允许存储 64 位整数（有符号或无符号）。

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            x= int(str(x)[::-1])
        else:
            x= -int(str(-x)[::-1])
        if x>=2**31-1 or x<=-2**31:
            return 0
        else:
            return x
def test1():
    s=Solution()
    print(s.reverse(1534236469))
    
test1()