# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root or not p: return None
        
        store = None
        s = root
        
        while s.val != p.val:
            if p.val <= s.val:
                store = s
                s=s.left
            else:
                s=s.right
            
        if not s.right:
            return store
        else:
            s=s.right
            while s.left:
                s=s.left
        return s
