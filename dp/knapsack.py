def knapshack(items:dict, maxWeight):
    sack = [ [0 for _ in range(maxWeight+1)] for _ in range(len(items)+1)]
    for i in range(1, len(items)+1):
        w = list(items.items())[i-1][0]
        p = list(items.items())[i-1][1]

        for j in range(1, maxWeight+1):
            if w <= j:
                sack[i][j] = max(sack[i-1][j-w]+p, sack[i-1][j])
            else:
                sack[i][j] = sack[i-1][j]
    return sack[-1][-1]

items = {5:60, 3:50, 4:70, 2:30}
print(knapshack(items, 5))
