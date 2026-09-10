# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        cur = root

        left, right = root.left, root.right
        cur.right = self.invertTree(left)
        cur.left  = self.invertTree(right)

        return root