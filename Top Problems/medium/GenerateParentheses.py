class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.helper(n, n, '', result)
        return result
    
    def helper(self, left, right, cur, result):
        if left==right==0:
            result.append(cur)
        else:
            if left > 0:
                self.helper(left-1,right,cur+'(', result)
            if right>left:
                self.helper(left, right-1, cur+')', result)
