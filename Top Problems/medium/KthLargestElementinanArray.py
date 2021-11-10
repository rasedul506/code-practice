class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        if len(nums)<k: return -1
        heapq.heapify(nums)
        size=len(nums)-k
        for i in range(size):
            heapq.heappop(nums)
        return nums[0]
        
#         #if len(nums)==k==1: return 1 
#         self.mergeSort(nums)
#         return nums[-k]
    
#     def mergeSort(self,nums):
#         if len(nums)>1:
#             med=len(nums)//2
#             LST=nums[:med]
#             RST=nums[med:]
            
#             self.mergeSort(LST)
#             self.mergeSort(RST)
            
#             i=j=k=0
            
#             while i<len(LST) and j<len(RST):
#                 if LST[i]<RST[j]:
#                     nums[k]=LST[i]
#                     i+=1
#                 else:
#                     nums[k]=RST[j]
#                     j+=1
#                 k+=1
#             while i<len(LST):
#                 nums[k]=LST[i]
#                 i+=1
#                 k+=1
#             while j<len(RST):
#                 nums[k]=RST[j]
#                 j+=1
#                 k+=1
