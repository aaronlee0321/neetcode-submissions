# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 

        curr = head
        stack = []

        while curr.next:
            stack.append(curr)
            curr = curr.next
        
        head = curr
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        
        curr.next = None
        return head