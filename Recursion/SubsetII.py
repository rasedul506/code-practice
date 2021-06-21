class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = [[]]
        
        for num in nums:
            length = len(result)
            for i in range(length):
                subset = result[i]+[num]
                if subset not in result:
                    result.append(subset)
        return result
