class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        puzzle=[[0 for _ in range(m+1)] for _ in range(n+1)]
        for j in range(1,n+1):
            for i in range(1,m+1):
                if i==1 and j==1:
                    puzzle[j][i]=1
                else:
                    puzzle[j][i]=puzzle[j-1][i]+puzzle[j][i-1]
                print(puzzle)
        return puzzle[n][m]
