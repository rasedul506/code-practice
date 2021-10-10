class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0) + 1
        for key, value in counter.items():
            if value == 1:
                return s.find(key)
        return -1
