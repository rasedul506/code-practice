# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        
        med=len(nums)//2
        root=TreeNode(nums[med])
        root.left=self.sortedArrayToBST(nums[:med])
        root.right=self.sortedArrayToBST(nums[med+1:])
        
        return root
        
