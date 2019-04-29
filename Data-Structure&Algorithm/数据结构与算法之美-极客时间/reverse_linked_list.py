'''
题目描述：对于给定的链表。反转链表
例子：
    输入：1->2->3->4->5->NULL
    输出：5->4->3->2->1->NULL
提示：
    分别使用迭代和递归实现
'''
import pysnooper
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    @pysnooper.snoop()
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next = curr
        return prev

# def main():
#     head = [1,2,3,4,5]
#     revers
    