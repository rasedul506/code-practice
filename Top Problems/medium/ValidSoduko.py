class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = [[] for _ in range(9)]
        seen_col = [[] for _ in range(9)]
        seen_block = [[] for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    b = r // 3 * 3 + c //3
                    
                    if num in seen_row[r] or num in seen_col[c] or num in seen_block[b]:
                        return False
                
                    seen_row[r].append(num)
                    seen_col[c].append(num)
                    seen_block[b].append(num)
        return True 
