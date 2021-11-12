class Solution:
    def searchRange(self, nums, target):
#         if not nums: return [-1,-1]
        
#         result = []
#         for i,val in enumerate(nums):
#             if val == target:
#                 result.append(i)
#         if not result:
#             return [-1, -1]
#         if len(result)<2:
#             return[result[0], result[0]]
#         return [result[0], result[-1]]
        
        def search(n):
            lo, hi = 0, len(nums)
            while lo<hi:
                mid = (lo+hi)//2
                if nums[mid] >= n:
                    hi=mid
                else:
                    lo=mid+1
            return lo
        lo = search(target)
        if target in nums[lo:lo+1]:
            return [lo, search(target+1)-1]
        else:
            return [-1, -1]
