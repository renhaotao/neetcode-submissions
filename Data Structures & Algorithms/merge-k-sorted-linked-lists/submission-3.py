# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # print(len(lists))
        # if len(lists) == 0:
        #     return None
        
        # if len(lists) == 1:
        #     return lists[0]

        n = len(lists)
        
        while n > 1:
        # for k in range(2):
            print(n)
            merged_list = []

            for i in range(0, n, 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < n else None

                list12 = self.mergeTwoLists(list1, list2)

                merged_list.append(list12)
            

            lists = merged_list
            n = len(lists)

        return lists[0] if lists else None

        

        




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
        