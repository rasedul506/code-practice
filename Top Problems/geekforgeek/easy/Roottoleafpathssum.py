# Your task is to complete this function
# function should return max sum level in the tree

def treePathSum(root):
    # Code here
    if not root:
        return
    result = []
    helper(root, '', result)
    return sum(result)

def helper(root, ns, result):   
    ns += str(root.data)
    
    if not root.left and not root.right:
        result.append(int(ns))
    if root.left:
        helper(root.left, ns, result)
    if root.right:
        helper(root.right, ns, result)
