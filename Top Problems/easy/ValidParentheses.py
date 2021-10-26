# class Solution:
#     def isValid(self, s: str) -> bool:
#         closing={')':'(', '}':'{', ']':'['}
#         opening=['(','{','[']
#         dlist=[]
#         pos=-1
        
#         for char in s:
#             if not dlist and char not in opening:
#                 return False
#             if char in opening:
#                 dlist.append(char)
#                 pos=len(dlist)-1
#             else:
#                 if closing[char]==dlist[pos]:
#                     dlist.pop(pos)
#                     pos-=1
#                 else:
#                     return False
#         return pos<0 and not dlist

class Solution:
    def isValid(self, s: str) -> bool:
        opening=['(','{','[']
        parentheses = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack:
                    return False
                match = stack.pop()
                if char != parentheses[match]:
                    return False
        return not stack
