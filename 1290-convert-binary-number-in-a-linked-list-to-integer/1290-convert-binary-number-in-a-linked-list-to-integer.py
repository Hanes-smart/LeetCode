# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        strs =""
        while head:
            strs += str(head.val)
            head = head.next
        decimal = int(strs,2)
        return decimal

        