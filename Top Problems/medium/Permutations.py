class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        result = []
        self.helper(nums, len(nums), [], [], result)
        return result
    
    def helper(self, nums, length, bucket, visited, result):
        if length == 0:
            result.append(bucket)
        else:
            for i in range(len(nums)):
                if i not in visited:
                    self.helper(nums,length-1, bucket+[nums[i]], visited+[i], result)
