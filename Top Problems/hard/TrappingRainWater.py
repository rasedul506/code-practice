# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height: return 0
#         waterUnit = 0
#         for i in range(1,len(height)-1):
#             minHeight = min(max(height[:i]), max(height[i+1:]))
#             captureWater = minHeight - height[i]
#             if captureWater > 0:
#                 waterUnit += captureWater
#         return waterUnit
  
 class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height)-1
        leftMax, rightMax=height[l], height[r]
        res = 0
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax,height[l])
                res += leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax, height[r])
                res += rightMax-height[r]
        return res  
