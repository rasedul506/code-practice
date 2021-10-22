# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        finlist=[]
        self.helper(root,1,finlist)
        return finlist
    
    def helper(self,root,level,res):
        if not root: return
        
        if level > len(res):
            res.append([root.val])
        else:
            res[level-1].extend([root.val])
        
        self.helper(root.left,level+1,res)
        self.helper(root.right,level+1,res)
    
