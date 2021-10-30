class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        
        i=j=0
        bucket=set()
        maxLength=0
        
        while j<len(s):
            if s[j] not in bucket:
                bucket.add(s[j])
                maxLength=max(maxLength,(j-i)+1)
                j+=1
            else:
                bucket.remove(s[i])
                i+=1
        return maxLength
