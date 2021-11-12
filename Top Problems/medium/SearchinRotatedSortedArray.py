class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        if len(nums)==1:
            if nums[0]!=target: return -1 
            else: return 0
        pivot=self.findpivot(nums,0,len(nums)-1)
        print(pivot)
        if target>=nums[0]:
            return self.searchTarget(nums,0,pivot-1,target)
        else:
            return self.searchTarget(nums,pivot,len(nums)-1,target)
    
    def findpivot(self,nums,start,end):
        if start<end:
            med=(start+end)//2
            
            # if nums[med]<nums[med-1]:
            #     return med
            if nums[med]>nums[med+1]:
                return med+1
            elif nums[0]<nums[med]:
                return self.findpivot(nums,med+1,end)
            else:
                return self.findpivot(nums,start,med)
        return len(nums)
    
    def searchTarget(self,nums,start,end,target):
        if start<=end:
            med=(start+end)//2
            
            if nums[med]==target:
                return med
            elif nums[med]<target:
                return self.searchTarget(nums,med+1,end,target)
            elif nums[med]>target:
                return self.searchTarget(nums,start,med-1,target)
        return -1
            
