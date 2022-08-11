#删除链表的倒数第 N 个结点
#给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# Definition for singly-linked list.
# from tools import * 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count=node_count(head)#计算链表长度
        if n>count:#如果n大于链表长度，则直接返回头结点,即不删除
            return head
        if n==count:#如果n等于链表长度，则直接删除头结点
            return head.next
        count=count-n+1#计算删除的位置
        return removeNthNode(head,count)# 删除链表的第 N 个结点

 # 计算链表长度
def node_count(head):
    count = 0
    while head:
        count+=1
        head = head.next
    return count  
# 删除第n个节点,返回head头节点
def removeNthNode(head,n):
    headcopy=head
    for i in range(n-2):#让headcopy走到第n-1个节点
        head=head.next#让headcopy走到第n-1个节点
    head.next=head.next.next#让headcopy走到第n个节点
    return headcopy
def printList(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()
def test1():
    head=ListNode(1,ListNode(2))
    head=ListNode(1,ListNode(2,ListNode(3)))
    # head=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    printList(Solution().removeNthFromEnd(head,1))
test1()