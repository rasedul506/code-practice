class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        if not nums and len(nums)<3: return result
        nums.sort()
    #     for i in range(len(nums)-2):
    #         if i>0 and nums[i]==nums[i-1]: continue 
    #         target=-nums[i]
    #         self.get2Sum(nums,i+1,len(nums)-1,target,result)
    #     return result
    # def get2Sum(self,nums,start,end,target,result):
    #     while end>start:
    #         val=nums[start]+nums[end]
    #         if val==target:
    #             result.append([-target,nums[start],nums[end]])
    #             start+=1
    #             end-=1
    #             while (end>start and nums[start]==nums[start-1]):
    #                 start+=1
    #             while (end>start and nums[end]==nums[end+1]):
    #                 end-=1
    #         elif val < target:
    #             start+=1
    #         elif val > target:
    #             end-=1
    
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: continue
            
            start=i+1
            end=len(nums)-1
            
            while start<end:
                if nums[i]+nums[start]+nums[end]==0:
                    result.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                    while(end>start and nums[start]==nums[start-1]):
                        start+=1
                    while(end>start and nums[end]==nums[end+1]):
                        end-=1
                elif nums[i]+nums[start]+nums[end] > 0:
                    end-=1
                elif nums[i]+nums[start]+nums[end]<0:
                    start+=1
        return result                 
        
        
