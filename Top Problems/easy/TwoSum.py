class Solution:
## Solution 1  
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
              return [i, j]
## Solution 2  
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        cache = {}
        for i in range(len(nums)):
            t = target-nums[i]
            if t not in cache:
                cache[nums[i]] = i
            else:
                return [cache[t], i]
