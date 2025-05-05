# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = ""
        head2 = ""
        
        # Collect digits from l1
        while l1:
            head1 += str(l1.val)
            l1 = l1.next
        
        # Collect digits from l2
        while l2:
            head2 += str(l2.val)
            l2 = l2.next
            
            sum_val = int(head1[::-1]) + int(head2[::-1])
            head3 = list(str(sum_val)[::-1])

        dummy = ListNode(0)
        current = dummy
        
        for digit in head3:
            current.next = ListNode(int(digit))
            current = current.next
        
        return dummy.next

        