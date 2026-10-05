# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        N = 1 

        cur = head

        while cur.next:
            N += 1 
            cur = cur.next

        i = 0 
        dummy = ListNode(None, head)
        pre = dummy
        cur = head
        
        while i < N-n: 
            pre = cur 
            cur = cur.next
            i += 1 

        tmp = cur.next 
        # cur.next = None
        pre.next = tmp
        
        
        return dummy.next 
        
       