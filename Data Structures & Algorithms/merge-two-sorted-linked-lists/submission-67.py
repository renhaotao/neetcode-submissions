# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Init
        dummy = ListNode(None)
        p1 = list1
        p2 = list2 

        pre = dummy 

        while p1 and p2: # end if one of the node is None
            if p1.val <= p2.val:
                tmp = p1.next 
                pre.next = p1 
                pre = p1 
                p1 = tmp 
            else:
                tmp = p2.next 
                pre.next = p2 
                pre = p2 
                p2 = tmp 

        print("pre.val", pre.val)

        if not p1 and p2: # p2 not none 
            pre.next = p2
            # return dummy.next
        elif not p2 and p1: # p2 not none 
            pre.next = p1
            # return dummy.next
        # else:
        return dummy.next


        print("pre.val", pre.val)
        # print("pre.next.val", pre.next.val)

        
        # if p2:
        #     pre.next = p1
        #     return dummy.next

        # if not p1:
        #     print("p1 not none")

        # if not p2:
        #     print("p2 not none")

        # if p1 and p2:
        #     return dummy.next 

        

        # print("pre:", pre.val)
        # # print("p2.val:", p2.val)
        # if p1 and not p2: # if p1 hit None 
        #     pre.next = p2 
        
        # if p2 and not p1:
        #     pre.next = p1 


        


        