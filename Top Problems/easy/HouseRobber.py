class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return
        if len(nums)<3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            for j in range(i-1):
                dp[i] = max(dp[i],dp[j]+nums[i])
        return max(dp)
        
