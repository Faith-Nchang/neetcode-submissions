# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(l, node, r):
            if not node:
                return True
            
            if not (l < node.val < r):
                return False
            return valid(l, node.left ,node.val) and valid(node.val, node.right, r)
        return valid(float('-inf'), root, float('inf'))