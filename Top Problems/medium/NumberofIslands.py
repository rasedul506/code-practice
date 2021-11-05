class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        island=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    island+=1
                    self.fillisland(grid,i,j)
        return island
    def fillisland(self,grid,i,j):
        
        if i>=len(grid) or i<0 or j >= len(grid[0]) or j<0 or grid[i][j]=='0':
            return
        elif grid[i][j]=='1':
            grid[i][j]='0'
            self.fillisland(grid,i,j+1)
            self.fillisland(grid,i,j-1)
            self.fillisland(grid,i+1,j)
            self.fillisland(grid,i-1,j)
