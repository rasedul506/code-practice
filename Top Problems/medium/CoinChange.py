class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        box = [sys.maxsize for _ in range(amount+1)]
        box[0] = 0
        length = len(box)

        for i in range(1,length):
            for coin in coins:
                if coin <= i:
                    box[i] = min(box[i-coin]+1, box[i])
                    
        return box[amount] if box[amount] != sys.maxsize else -1
