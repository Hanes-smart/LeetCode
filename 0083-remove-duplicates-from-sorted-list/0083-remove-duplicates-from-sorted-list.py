from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next  # skip duplicate
            else:
                curr = curr.next
        return head

# Helper function to create a linked list from list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print linked list as list
def print_linkedlist(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test cases
s = Solution()
head1 = list_to_linkedlist([1, 1, 2])
head2 = list_to_linkedlist([1, 1, 2, 3, 3])

print_linkedlist(s.deleteDuplicates(head1))  # Output: [1, 2]
print_linkedlist(s.deleteDuplicates(head2))  # Output: [1, 2, 3]
