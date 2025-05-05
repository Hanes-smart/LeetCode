# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count =0
        curr = head
        while curr:
            count +=1
            curr = curr.next
        count = (count//2)+1

        while (count-1) !=0 and head:
            head = head.next
            count -=1
        
        return head
        

