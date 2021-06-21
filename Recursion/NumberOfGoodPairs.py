# Number of Good Pairs
# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0

# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         goodPairs = 0
#         length = len(nums)
#         for i in range(length-1):
#             for j in range(i+1, length):
#                 if nums[i] == nums[j]:
#                     goodPairs += 1
#         return goodPairs
  
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = 0
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, value in dic.items():
            goodPairs += (value*(value-1))//2
        return goodPairs
  
