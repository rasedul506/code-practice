class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        y = 1
        if x < 0:
            y = -y
        x = abs(x)
        
        while (x != 0):
            r = r * 10 + x%10
            x = x//10
            
        if (-2**31) < r*y < (2**31)-1:
            return r * y
        return 0
