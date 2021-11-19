class Solution:
    
    #Function to find the number of 'X' total shapes.
	def xShape(self, grid):
		#Code here
		count = 0
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if grid[i][j] == 'X':
		            count += 1
		            self.helper(grid, i, j)
		return count
	def helper(self, grid, i, j):
	    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == '0':
	        return
	    elif grid[i][j] == 'X':
	        grid[i][j] = '0'
	        self.helper(grid, i+1, j)
	        self.helper(grid, i-1, j)
	        self.helper(grid, i, j-1)
	        self.helper(grid, i, j+1)
