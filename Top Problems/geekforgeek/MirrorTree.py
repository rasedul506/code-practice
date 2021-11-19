#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
    #     # Code here
    #     result = []
    #     return self.traversal(root, result)
    # def traversal(self, root, result):
    #     if root:
    #         return self.traversal(root.right, result)
    #         result.append(root.data)
    #         return self.traversal(root.left, result)
    #     return result
        if not root:
            return
        stack = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
