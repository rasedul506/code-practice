# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = -sys.maxsize
#         for i in range(len(nums)):
#             partial_sum = 0
#             for j in range(i,len(nums)):
#                 partial_sum += nums[j]
#                 max_sum=max(max_sum,partial_sum)
#         return max_sum
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        
        dp.append(nums[0])
        for i in range(1,len(nums)):
            dp.append(max(nums[i],dp[i-1]+nums[i]))
        return max(dp)
