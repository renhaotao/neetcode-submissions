# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre = None
        cur = head 

        i = 1 

        while cur: 
            print(i)
            tmp = cur.next 

            cur.next = pre 
            pre = cur 
            cur = tmp

            i += 1 

        return pre


        

   

