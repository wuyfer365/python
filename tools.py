class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
    # 添加节点到末尾
    def add(self, x):
        node = ListNode(x)
        if self.next is None:
            self.next = node
        else:
            self.next.add(x)


# 列表转数组
def listToArray(head):
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array
# 数组转链表
def arrayToList(array):
    head = ListNode(array[0])
    cur = head
    for i in range(1, len(array)):
        cur.next = ListNode(array[i])
        cur = cur.next
    return head

# 数组转字符串
def arrayToString(array):
    return ''.join(str(i) for i in array)
# 字符串转数组
def stringToArray(num):
    return list(num)
# 数字转链表,逆序以字符串存储    
def numToList(num):
    num=numToString(num)
    num=stringToReverse(num)
    num=stringToArray(num)        
    return arrayToList(num)
# 数字转字符串

def numToString(num):
    return str(num)
# 打印链表

def printList(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

# 字符串反转
def stringToReverse(num):
    return str(num)[::-1]


# 数组转数字
def arrayToNum(self, array):
    num = 0
    for i in range(len(array)):
        num += array[i] * pow(10, len(array) - i - 1)
    return num

# 计算链表长度
def node_count(head):
    count = 0
    while head:
        count+=1;
        head = head.next
    return count
