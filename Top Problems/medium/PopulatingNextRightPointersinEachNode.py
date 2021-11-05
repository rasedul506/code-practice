"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        
        bucket=[]
        self.helper(root, 1, bucket)
        
        return root
    
    def helper(self, root,level, bucket):
        if not root:
            return
        if level>len(bucket):
            bucket.append([root])
        else:
            bucket[level-1][-1].next = root
            bucket[level-1].extend([root])
        self.helper(root.left, level+1, bucket)
        self.helper(root.right, level+1, bucket)
