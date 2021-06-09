# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

# Example 1:

# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 4
# https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3230/


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        low=0
        maxcount=0
        zerocount=0
        k=1
        for i in range(len(nums)):
            if nums[i] == 0:
                zerocount += 1
            while zerocount > k:
                if nums[low] == 0:
                    zerocount -= 1
                low += 1
            maxcount=max(maxcount,i-low+1)
        return maxcount
                    
