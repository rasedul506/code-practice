class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        if l < 2:
            return True
        p = 0
        q = l - 1
        
        while (p<q):
            while p<q and not s[p].isalnum():
                p += 1
            while p<q and not s[q].isalnum():
                q -= 1
            if s[p].lower() != s[q].lower():
                return False
            p += 1
            q -= 1
        return True
            
        
        
