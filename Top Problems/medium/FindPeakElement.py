class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums: return -1
        if len(nums)==1: return 0
        if len(nums)==2 and nums[0]>nums[1]: return 0 
        if len(nums)==2 and nums[0]<nums[1]: return 1 
        
        med = len(nums)//2
        if nums[med-1] < nums[med] > nums[med+1]:
            return med
        elif nums[med]<nums[med+1]:
            return self.findpeak(nums, med+1, len(nums)-1)
        elif nums[med]<nums[med-1]:
            return self.findpeak(nums, 0, med-1)
    
    def findpeak(self, nums, start, end):
        while start<end:
            if nums[start]>nums[start+1]:
                return start
            start += 1
        return end
