# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    # self.level = 0

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return_list = []
        dq = deque()
        if root:
            dq.append(root)

        # while root:

        while len(dq) > 0:
            lvl_list = []
            length = len(dq)
            for i in range(length):
                # node_i = dq[i]
                # print("appending", node_i.val)

                current = dq.popleft()
                lvl_list.append(current.val)
                # print("current", current.val)
            

                if current.left:
                    dq.append(current.left)

                if current.right:
                    dq.append(current.right)

                # for nd in dq:
                #     print(nd.val)
                # print()

            return_list.append(lvl_list)
            # print(self.return_list)

        return return_list

           

        
