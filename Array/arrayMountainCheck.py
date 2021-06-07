# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true
# https://leetcode.com/explore/featured/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        ptr = 0
        
        for i in range (1, length):
            if arr[i] > arr[i-1]:
                ptr += 1
        if ptr == 0 or ptr == length-1:
            return False
        for j in range(ptr+1, length):
            if arr[j] < arr[j-1]:
                ptr += 1
        return ptr == length-1
