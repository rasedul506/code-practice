import sys

def coinChange(coins, amount):
    if not coins or not amount:
        return
    
    box = [sys.maxsize for _ in range(amount+1)]
    box[0] = 0
    length = len(box)

    for i in range(1,length):
        for coin in coins:
            if coin <= i:
                box[i] = min(box[i-coin]+1, box[i])
    return box[-1]

print(coinChange([1,2,5], 11))
