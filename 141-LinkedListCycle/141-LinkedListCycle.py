# Last updated: 24/11/2025, 17:26:59
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
            if head is temp:
                return True
        return False