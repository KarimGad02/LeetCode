# Last updated: 24/11/2025, 17:26:46
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        def recursion(head):
            if head is None or head.next is None:
                return head
            reversed_list = recursion(head.next)
            head.next.next = head
            head.next = None
            return reversed_list
        return recursion(head)