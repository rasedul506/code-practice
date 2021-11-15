class Solution:
    def titleToNumber(self, s: str) -> int:
        if len(s)==0: return 0
        result = 0
        times = len(s) -1
        
        for char in s:
            result = result + 26**times*(ord(char)-64)
            times -= 1
        return result
