# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1 
            cur = cur.next

        print("L=", length)

        idx_rm = length - n
        if length == 1:
            head = None
        elif idx_rm ==0:
            return head.next
        else:
            i = 0 
            pre, cur = None, head 
            while cur:
                print(i, cur.val)

                if i == idx_rm:
                    nxt = cur.next # is none 
                    cur.next = None
                    pre.next = nxt

                    return head 

                pre = cur 
                print("Setting pre to", cur.val)
                cur = cur.next
                
                i += 1
                
        
        return head 
            # if i == n:
            #     return cur.val == n
            