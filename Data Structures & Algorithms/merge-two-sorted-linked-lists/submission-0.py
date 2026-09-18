# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #deciding on the head
        head = None
        curr = None
        while list1 and list2:
            val1 = 0
            val2 = 0        
            if list1:
                val1 = list1.val
            if list2:
                val2 = list2.val

            if val1 > val2:
                if not head:
                    head = list2
                    curr = head
                    print("here1",head.val)
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next
            else:
                if not head:
                    head = list1
                    curr = head
                    print("here2",head.val)
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next

        if list1:
            if not head:
                head = list1
                curr = head
            else:
                curr.next = list1
        elif list2:
            if not head:
                head = list2
                curr = head
            else:
                curr.next = list2

        return head