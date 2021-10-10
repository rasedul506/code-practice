class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        
        for i in range(N//2 + N%2):
            for j in range(N//2):
                tmp = matrix[N-1-j][i]
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
                matrix[j][N-1-i] = matrix[i][j]
                matrix[i][j] = tmp
        
