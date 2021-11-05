class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numBox={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result=[]
        self.backtracking(numBox,digits,0,'',result)
        return result
    def backtracking(self,numBox,digits,index,cur,result):
        if index==len(digits):
            result.append(cur)
        else:
            for letter in numBox[digits[index]]:
                self.backtracking(numBox,digits,index+1,cur+letter,result)
        
        
