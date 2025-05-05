class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = ListNode(0)
        prev.next = head
        dummy = prev

        while head and head.next:
            first = head
            second = head.next

            # Swap nodes
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers
            prev = first
            head = first.next

        return dummy.next
