class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        pointer=0
        
        while pointer<=high:
                if nums[pointer]==0:
                    nums[low], nums[pointer]=nums[pointer], nums[low]
                    low+=1
                    pointer+=1
                elif nums[pointer]==1:
                    pointer+=1
                elif nums[pointer]==2:
                    nums[high], nums[pointer]=nums[pointer], nums[high]
                    high-=1
                
