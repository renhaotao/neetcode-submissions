# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy 

        run = 0
        while list1 and list2:
            print(list1.val, list2.val)

            if list2.val > list1.val:
                tail.next = list1
                list1 = list1.next
                # list1 = 
            elif list2.val <= list1.val:
                tail.next = list2 
                list2 = list2.next

            tail = tail.next 

            print(run)
            run+= 1 
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
        