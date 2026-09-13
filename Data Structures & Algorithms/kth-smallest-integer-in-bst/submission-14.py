# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        int_list = []
        def helper(node):
            if not node:
                return 

            # print("node.val:", node.val)
            # int_list.append(node.val)
            helper(node.left)
            int_list.append(node.val)
            # print("int_list (after left):", int_list)

            helper(node.right)

            return 
            # print("int_list (after right)", int_list)
            # print("node.val 2:", node.val)

            # return 
        helper(root)

        print("int_list (final)", int_list)

        return int_list[k-1]
        