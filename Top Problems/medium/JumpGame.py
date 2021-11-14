class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length=len(nums)
        if not nums or length==0: return False
        if length==1: return True
        if length==2: return nums[0]>=1
        
    #     return self.jumping(0,nums)
    # def jumping(self,index,nums):
    #     if index<len(nums):
    #         if index==len(nums)-1: return True
    #         n=nums[index]
    #         for i in range(1,n+1):
    #             return self.jumping(i,nums)
    #     else: return
    #####recurssive
#         bucket=[False for _ in range(len(nums))]
#         self.jumpping(0,nums,bucket)
#         return bucket[-1]
    
#     def jumpping(self,index,nums,bucket):
#         if index<len(nums):
#             if bucket[index]==True or bucket[-1]==True: return
#             bucket[index]=True
#             n=nums[index]
#             for i in reversed(range(1,n+1)): 
#                 if index+i < len(nums) and bucket[index+i]==False:
#                     self.jumpping(index+i,nums,bucket)
#         else: return
    #####
        # i=highjump=0
        # while i<=highjump:
        #     highjump=max(highjump,i+nums[i])
        #     if highjump>=len(nums)-1: return True
        #     i+=1
        # return False
        minjump=[11111001 for i in range(len(nums))]
        minjump[0]=0
        
        for p in range(1,len(nums)):
            for q in range(0,p):
                if q+nums[q]>=p:
                    minjump[p]=min(minjump[q]+1,minjump[p])
        return minjump[-1]< 11111001
