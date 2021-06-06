# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
  
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums: return
        
        count = 0
        maxConsecutive = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxConsecutive = max(maxConsecutive, count)
            else:
                count = 0
        return maxConsecutive
