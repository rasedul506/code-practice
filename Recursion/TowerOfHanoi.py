
def towerOfHanoi(n: int, source: str, destination: str, aux: str):
    if n == 1:
        print("{}=>{}".format(source, destination))
        return
    towerOfHanoi(n-1,source, aux, destination)
    print("{}=>{}".format(source, destination))
    towerOfHanoi(n-1, aux, destination, source)

def TowerOfHanoi(n: int, source: str, destination: str, aux: str):
    if n == 1:
        return 1
    return TowerOfHanoi(n-1, source, aux, destination) + 1 + TowerOfHanoi(n-1, aux, destination, source)

    
n = 8
print(TowerOfHanoi(n,'A','C','B'))

towerOfHanoi(n,'A','C','B')
