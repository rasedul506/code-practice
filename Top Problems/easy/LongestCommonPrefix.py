class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs: return ''
        for index, word in enumerate(zip(*strs)):
            if len(set(word)) > 1:
                return strs[0][:index]
        else:
            return min(strs)
