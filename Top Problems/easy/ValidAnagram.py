class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i],0) + 1
        
        for j in range(len(t)):
            if not counter.get(t[j]):
                return False
            counter[t[j]] = counter.get(t[j]) - 1
        for value in counter.values():
            if value != 0:
                return False
        return True
