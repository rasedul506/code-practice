class Solution:
    def longestPalindrome(self, s: str) -> str:
        # babcc
        if len(s) == 0: return 0
        
        maxLengthString = ''
        
        for i in range(len(s)):
            substring = ''
            for j in range(i,len(s)):
                substring += s[j]
                if substring == substring[::-1] and len(substring) > len(maxLengthString):
                    maxLengthString = substring
        return maxLengthString
