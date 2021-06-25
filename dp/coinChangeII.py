def coinChangeII(coins, amount):
    if not coins or not amount: return

    box = [ [ 0 for _ in range(amount+1)] for _ in range(len(coins)+1) ]
    for b in box:
        b[0] = 1
    
    for i in range(1,len(coins)+1):
        for j in range(amount+1):
            if coins[i-1] <= j:
                box[i][j] = box[i][j-coins[i-1]]+box[i-1][j]
            else:
                box[i][j] = box[i-1][j]
    
    print(box)

print(coinChangeII([1,2,5], 5))
