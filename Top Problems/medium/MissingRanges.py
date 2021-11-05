class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower)+'->'+str(upper)]
        res = []
        for i in range(len(nums)):
            if lower==nums[i]-1:
                res.append(str(lower))
            elif lower < nums[i]-1:
                res.append(str(lower)+'->'+str(nums[i]-1))
            lower = nums[i]+1
        if upper > lower:
            res.append(str(lower)+'->'+str(upper))
        elif upper == lower:
            res.append(str(lower))
        return res
