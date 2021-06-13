class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = []
        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row)-1):
                row[j] = pascals[i-1][j-1] + pascals[i-1][j]
            pascals.append(row)
        return pascals
