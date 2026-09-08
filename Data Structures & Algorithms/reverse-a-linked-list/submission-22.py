# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev_n = None
        cur_n = head 

        while cur_n:
            print(cur_n.val)

            next_n_save = cur_n.next # save the next node 
            cur_n.next = prev_n # flip the pointer from n -> n+1 to n -> n-1

            prev_n = cur_n
            cur_n = next_n_save




   
        return prev_n
        
        # # initial readout 
        # cur_n_ro = head 
        # while cur_n_ro is not None:
        #     print(cur_n_ro.val)
        #     cur_n_ro = cur_n_ro.next
        # print()

        # head_save = head 

        # cur_n = head 

        # while cur_n.next is not None:
        #     print("Next node's val=", cur_n.next.val)
        #     next_n_val_save = cur_n.next.val
        #     cur_n.next.val = cur_n.val

        #     cur_n = cur_n.next


        # # readout 
        # cur_n_ro = head 
        # while cur_n_ro is not None:
        #     print(cur_n_ro.val)
        #     cur_n_ro = cur_n_ro.next

        # return head

        

