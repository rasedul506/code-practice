class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowset=set()
        colset=set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowset.add(i)
                    colset.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowset or j in colset:
                    matrix[i][j]=0
