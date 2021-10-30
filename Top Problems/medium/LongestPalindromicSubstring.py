# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # babcc
#         if len(s) == 0: return 0
        
#         maxLengthString = ''
        
#         for i in range(len(s)):
#             substring = ''
#             for j in range(i,len(s)):
#                 substring += s[j]
#                 if substring == substring[::-1] and len(substring) > len(maxLengthString):
#                     maxLengthString = substring
#         return maxLengthString

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # babcc
        if len(s) <2:
            return s
        
        n = len(s)
        
        table = [[0 for _ in range(n)] for _ in range(n)]
        
        maxLength = 1
        i = 0
        while i<n:
            table[i][i] = True
            i+=1
        
        start = 0
        i = 0
        while i<n-1:
            if s[i]==s[i+1]:
                table[i][i+1]=True
                maxLength = 2
                start = i
            i+=1
        k = 3
        while k <= n:
            i = 0
            while i<n-k+1:
                j = i+k-1
                if s[i] == s[j] and table[i+1][j-1]:
                    table[i][j] = True
                    
                    if k>maxLength:
                        maxLength = k
                        start = i
                i+=1
            k+=1
                
        return s[start:start+maxLength]
                    
