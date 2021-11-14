class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        bucket = [1 for _ in range(len(nums))]
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    bucket[i] = max(bucket[i], bucket[j]+1)
        
        return max(bucket)
