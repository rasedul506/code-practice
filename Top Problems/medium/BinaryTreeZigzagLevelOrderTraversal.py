# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        s1,s2=[],[]
        res = []
        s1.append(root)
        
        while s1 or s2:
            b1 = []
            b2 = []
            while s1:
                node = s1.pop()
                b1.append(node.val)
                if node.left:
                    s2.append(node.left)
                if node.right:
                    s2.append(node.right)
            if b1:
                res.append(b1)
            while s2:
                node = s2.pop()
                b2.append(node.val)
                if node.right:
                    s1.append(node.right)
                if node.left:
                    s1.append(node.left)
            if b2:
                res.append(b2)
        return res
                
        
        
