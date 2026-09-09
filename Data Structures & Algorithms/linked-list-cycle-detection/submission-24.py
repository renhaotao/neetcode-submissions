# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head 
        # print(slow.val, fast.val, fast.next.val)
        while slow and fast.next:
            slow = slow.next 

            if not fast.next.next:
                return False
            fast = fast.next.next 
            print(slow.val, fast.val)

            if slow == fast:
                return True

        return False