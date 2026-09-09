# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0 
        cur = head 
        while cur:
            length += 1 
            cur = cur.next 
        
        print("Length: ", length)
    
        counter = 0 
        cur = head 
        pre = None
        while counter < length / 2:
            counter += 1 
            pre = cur
            cur = cur.next 
        pre.next = None
        second_tail = cur


        second_prev, second_cur = None, second_tail
        while second_cur:
            second_nxt = second_cur.next
            second_cur.next = second_prev

            second_prev = second_cur 
            second_cur = second_nxt

        second_lead = second_prev
        
        # print("Check second part")
        # cur2 = second_lead
        # while cur2:
        #     print(cur2.val)
        #     cur2 = cur2.next

        # now put them together 
        cur1, cur2 = head, second_lead
        save_head = head 

        while cur1 and cur2:
            cur1_nxt, cur2_nxt = cur1.next, cur2.next 
            cur1.next = cur2
            cur2.next = cur1_nxt

            cur1, cur2 = cur1_nxt, cur2_nxt

        # print("Check full list")
        cur_full = save_head
        while cur_full:
            cur_full = cur_full.next