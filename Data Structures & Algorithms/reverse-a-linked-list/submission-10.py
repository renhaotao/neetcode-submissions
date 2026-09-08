# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return head
        else:
        # print(head.val)
            current_node = head 

            new_array = []

            while current_node.next is not None:
                new_array.append(current_node.val)
                current_node = current_node.next 

            new_array.append(current_node.val)

            print(new_array)
            new_array = new_array[::-1]
            print(new_array)

            current_node = head 
            print("current_node has val:", current_node.val)
            i = 0

            while current_node.next is not None:
                print("current_node has val:", current_node.val)

                current_node.val = new_array[i]
                print("Set it to val=", current_node.val)
                current_node = current_node.next
                print("Next node has val=", current_node.val)

                i += 1 

            current_node.val = new_array[i]

            

        return head

        

