class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p = 0
        q = len(numbers) - 1
        
        while (p<q):
            if numbers[p] + numbers[q] == target:
                return [p+1,q+1]
            elif numbers[p] + numbers[q] < target:
                p += 1
            elif numbers[p] + numbers[q] > target:
                q -= 1
