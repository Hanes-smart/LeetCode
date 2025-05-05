# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        new_head = head.next
        curr = head 
        prev = None
        while curr and curr.next:
            next_pair = curr.next.next
            second = curr.next # think of val(assigning)
            second.next = curr
            curr.next = next_pair
            if prev:
                prev.next = second
            prev = curr
            curr = next_pair
        return new_head
            
            
        
        