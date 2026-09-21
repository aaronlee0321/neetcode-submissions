from collections import defaultdict
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first_ptr = head
        if first_ptr and first_ptr.next:
            second_ptr = head.next
        else:
            return False

        while second_ptr and second_ptr.next and second_ptr.next.next:
            if second_ptr == first_ptr:
                return True
            
            second_ptr = second_ptr.next.next
            first_ptr = first_ptr.next

        return False
                
            
