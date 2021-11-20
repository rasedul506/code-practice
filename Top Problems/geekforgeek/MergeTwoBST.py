class Solution:
    
    #Function to return a list of integers denoting the node 
    #values of both the BST in a sorted order.
    def merge(self, root1, root2):
        #code here.
        ar1 = []
        ar2 = []
        result = []
        self.inorder(root1, ar1)
        self.inorder(root2, ar2)
        p=q=0
        while p<len(ar1) and q<len(ar2):
            if ar1[p]<ar2[q]:
                result.append(ar1[p])
                p += 1
            else:
                result.append(ar2[q])
                q += 1
        if p<len(ar1):
            result.extend(ar1[p:])
        else:
            result.extend(ar2[q:])
        return result
        
    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.data)
            self.inorder(root.right, result)
