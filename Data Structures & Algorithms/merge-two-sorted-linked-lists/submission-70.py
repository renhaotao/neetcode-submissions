# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode() # None 
        pre = dummy 
        p1, p2 = list1, list2 

        while p1 and p2:
            
            if p1.val <= p2.val:
                # tmp = p1.next 
                pre.next = p1 
                pre = p1 
                p1 = p1.next
                # p1 = tmp 
            else:
                # tmp = p2.next 
                pre.next = p2 
                pre = p2
                p2 = p2.next
                # p2 = tmp 

        if p2:
            pre.next = p2 
        else:
            pre.next = p1 


        return dummy.next
        

       

        