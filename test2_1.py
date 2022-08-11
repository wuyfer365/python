# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(1 -> 2 -> 3) + (4 -> 5 -> 6)
# 输出：(9 -> 7 -> 5)
# 解释：321 + 654 = 975

from tools import *

class Solution:
    
    # 两个数字相加
    def addTwoNumbers(self, l1, l2):
        """ 
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a1=listToArray(l1)
        s1=arrayToString(a1)
        i1=int(stringToReverse(s1))#反转
        a2=listToArray(l2)
        s2=arrayToString(a2)
        i2=int(stringToReverse(s2))#反转
        i3=i1+i2 
        print(i3)
        #数字i3转字符串
        s3=numToString(i3)
        #字符串s3反转
        s3=stringToReverse(s3)
        return arrayToList(stringToArray(s3))


def test1():
    s=Solution()
    l1 = numToList(753865680)  
    l2 = numToList(798580876)
    printList(l1)
    printList(l2)
    l3 = s.addTwoNumbers(l1, l2)
    printList(l3)  

test1()