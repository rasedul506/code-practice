class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for x in nums:
            length = len(result)
            for i in range(length):
                result.append(result[i] + [x])
        return result
    
#         res = []
#         subset = []
        
#         def dfs(i):
#             if i>=len(nums):
#                 res.append(subset.copy())
#                 return
#             subset.append(nums[i])
#             dfs(i+1)
            
#             subset.pop()
#             dfs(i+1)
        
#         dfs(0)
#         return res
