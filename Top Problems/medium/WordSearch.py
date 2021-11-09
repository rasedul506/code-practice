class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.findword(board, row, col, word):
                    return True
        return False
    
    def findword(self, board, row, col, word):
        if len(word)==0:
            return True
        
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or board[row][col] != word[0]:
            return False
        
        temp = board[row][col]
        board[row][col] = ''
        
        result = self.findword(board, row+1, col, word[1:]) or \
                 self.findword(board, row-1, col, word[1:]) or \
                 self.findword(board, row, col+1, word[1:]) or \
                 self.findword(board, row, col-1, word[1:])
        
        board[row][col] = temp
        
        return result
