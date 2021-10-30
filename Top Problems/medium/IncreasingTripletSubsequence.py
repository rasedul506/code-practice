class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3: return False
        
        min1 = sys.maxsize
        min2 = sys.maxsize
        
        for num in nums:
            if num>min2:
                return True
            elif num<min1:
                min1=num
            elif num>min1 and num<min2:
                min2=num
        return False
            
