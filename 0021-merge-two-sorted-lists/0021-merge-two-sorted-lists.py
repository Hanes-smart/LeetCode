# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None ):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head is None:
            self.head = ListNode(val, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = ListNode(val, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.push(data)

    def print(self):

        itr = self.head
        llstr = []
        while itr:
            llstr.append(itr.val)
            itr = itr.next
        return llstr

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()  # Dummy node to start the merged list
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # One of list1 or list2 is now None, attach the remaining
        tail.next = list1 if list1 else list2

        return dummy.next
List1 = [1,2,4]
List2 = [1,3,4]