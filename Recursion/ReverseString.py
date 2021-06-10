# Write a function that reverses a string. The input string is given as an array of characters s.


# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
  
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(p, q, s):
            if p<q:
                s[p], s[q] = s[q], s[p]
                reverse(p+1, q-1, s)
        return reverse(0, len(s)-1, s)
        
