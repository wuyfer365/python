from tools import *    
# 示例：
# 输入：(1 -> 2 -> 3) + (4 -> 5 -> 6)
# 输出：(9 -> 7 -> 5)
# 解释：321 + 654 = 975

class Solution:
    
    # 两个数字相加
    def addTwoNumbers(self, l1, l2):
        pre=ListNode(0)
        head1=l1
        head2=l2
        carry=0
        l1_node_count=node_count(l1)# 计算链表1的长度
        l2_node_count=node_count(l2)# 计算链表2的长度
        if l1_node_count>l2_node_count:# 如果链表1的长度大于链表2的长度，则循环次数为链表2的长度
            for i in range(l2_node_count):#l2的长度
                currentsum=int(l1.val)+int(l2.val)+carry
                l1.val=str(currentsum%10)
                if currentsum>=10:
                    carry=1
                else:
                    carry=0
                l1=l1.next
                if i<=l2_node_count-1:
                    l2=l2.next
            if carry==1:# 如果链表1的长度大于链表2的长度，则需要将链表1的剩余部分进行相加
                while l1!=None:
                    currentsum=int(l1.val)+carry
                    l1.val=str(currentsum%10)
                    if currentsum>=10:
                        carry=1
                    else:
                        carry=0
                        break
                    pre=l1
                    l1=l1.next
                else:
                    if carry==1:#最后一位进位
                        pre.next=ListNode(1)
            return head1
        elif l1_node_count==l2_node_count:
            for i in range(l2_node_count):
                currentsum=int(l1.val)+int(l2.val)+carry
                l1.val=currentsum%10
                if currentsum>=10:
                    carry=1
                else:
                    carry=0
                if i==l2_node_count-1:
                    pre=l1
                l1=l1.next
                l2=l2.next
            if carry==1:
                pre.next=ListNode(1)
            return head1
        else:
            for i in range(l1_node_count):
                currentsum=int(l1.val)+int(l2.val)+carry
                l2.val=currentsum%10
                if currentsum>=10:
                    carry=1
                else:
                    carry=0
                l2=l2.next
                if i<=l1_node_count-1:
                    l1=l1.next
            if carry==1:# 如果链表1的长度大于链表2的长度，则需要将链表1的剩余部分进行相加
                while l2!=None:
                    currentsum=int(l2.val)+carry
                    l2.val=str(currentsum%10)
                    if currentsum>=10:
                        carry=1
                    else:
                        carry=0
                        break
                    pre=l2
                    l2=l2.next
                else:
                    if carry==1:#最后一位进位
                        pre.next=ListNode(1)    
            return head2
        
def test1():
    s=Solution()
    l1 = numToList(753865680)  
    l2 = numToList(798580876)
    printList(l1)
    printList(l2)
    l3 = s.addTwoNumbers(l1, l2)
    printList(l3) 

test1()


