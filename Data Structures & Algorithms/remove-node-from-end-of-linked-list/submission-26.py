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


        dummy = ListNode(0, head)
        pre = dummy 
        for _ in range(length-n):
            pre = pre.next

        pre.next = pre.next.next
        
        return dummy.next
        # idx_rm = length - n
        # if idx_rm==0:
        #     return head.next
        # else:
        #     i = 0 
        #     pre, cur = dummy, head 
        #     while cur:
        #         # print(i, cur.val)
                
        #         if i == idx_rm:
        #             nxt = cur.next # is none 
        #             cur.next = None
        #             pre.next = nxt

        #             return head 

        #         pre = cur 
        #         cur = cur.next
                
        #         i += 1
                    
        
        # return head 
          