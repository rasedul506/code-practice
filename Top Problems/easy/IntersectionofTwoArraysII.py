class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)
        
        cache = {}
        for num in nums1:
            cache[num] = cache.get(num, 0) + 1
        result = []
        for num in nums2:
            val = cache.get(num)
            if val and val >0:
                result.append(num)
                cache[num] -= 1
        return result
   

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
#         if len(nums1) < len(nums2):
#             return self.intersect(nums2, nums1)
        
#         cache = {}
#         for num in nums1:
#             cache[num] = cache.get(num, 0) + 1
#         result = []
#         for num in nums2:
#             val = cache.get(num)
#             if val and val >0:
#                 result.append(num)
#                 cache[num] -= 1
#         return result
        n1 = sorted(nums1)
        n2 = sorted(nums2)
        i = j = k = 0
        result = []
        while(i<len(n1) and j<len(n2)):
            if n1[i] < n2[j]:
                i += 1
            elif n1[i] > n2[j]:
                j += 1
            elif n1[i] == n2[j]:
                result.append(n1[i])
                i += 1
                j += 1
        return result
