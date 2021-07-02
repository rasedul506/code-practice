# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.preOrderTraversal(root, [])
    
    def preOrderTraversal(self, root: TreeNode, result):
        if root:
            result.append(root.val)
            self.preOrderTraversal(root.left, result)
            self.preOrderTraversal(root.right, result)
            if result:
                return result
            
 
