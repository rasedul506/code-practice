class Solution:
    def romanToInt(self, s: str) -> int:
        roman = 0
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
        for i in range(len(s)):
            if i!=0 and d[s[i]]>d[s[i-1]]:
                roman += d[s[i]]-d[s[i-1]]-d[s[i-1]]
            else:
                roman += d[s[i]]
        return roman
                
