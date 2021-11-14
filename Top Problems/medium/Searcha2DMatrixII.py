class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not target: return False
        
        return self.findTarget(matrix,0,len(matrix[0])-1,target)
        
    def findTarget(self,matrix,row,col,target):
        if col<0 or row<0 or row>len(matrix)-1 or col>len(matrix[0])-1:
            return False
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]>target:
            return self.findTarget(matrix,row,col-1,target)
        elif matrix[row][col]<target:
            return self.findTarget(matrix,row+1,col,target)
