# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        sizeA = 0
        sizeB = 0
        skipsA = 0
        skipsB = 0
        currA = headA
        currB = headB
        while currA:
            sizeA += 1
            currA = currA.next
        while currB:
            sizeB += 1
            currB = currB.next
        align = sizeA - sizeB
        currA = headA
        currB = headB
        if align > 0:
            for _ in range(abs(align)):
                currA = currA.next
            skipsA += align
        if align < 0:
            for _ in range(abs(align)):
                currB = currB.next
            skipsB += align
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None