# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root or k==0: return None
#         result = []
        
#         self.helper(root,result)
#         return result[k-1]
    
#     def helper(self,root,result):
#         if root:
#             self.helper(root.left, result)
#             result.append(root.val)
#             self.helper(root.right, result)        
        stack = []
        
        cur = root
        
        while cur:
            stack.append(cur)
            cur = cur.left
        
        i = 0
        while stack and i<k:
            n = stack.pop()
            i+=1
            
            right=n.right
            while right:
                stack.append(right)
                right = right.left
        return n.val
