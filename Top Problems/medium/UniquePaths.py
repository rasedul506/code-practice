class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        puzzle = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1, n+1):
                if i==j==1:
                    puzzle[i][j]=1
                else:
                    puzzle[i][j]=puzzle[i-1][j]+puzzle[i][j-1]
        return puzzle[m][n]
