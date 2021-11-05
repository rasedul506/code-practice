# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None
        
        mapping = {}
        
        for i,v in enumerate(inorder):
            mapping[v] = i
        
        def conTree(start, end):
            if start>end: return None
            root = TreeNode(preorder.pop(0))
            index = mapping[root.val]
            root.left = conTree(start, index-1)
            root.right = conTree(index+1, end)
            
            return root
        
        return conTree(0, len(inorder)-1)
        
            
        
