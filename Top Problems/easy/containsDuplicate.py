class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsset = set(nums)
        return len(nums) != len(numsset)
      

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        for values in dic.values():
            if values > 1:
                return True
        return False
        
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         cache = []
#         for num in nums:
#             if num in cache:
#                 return True
#             cache.append(num)
#         return False
