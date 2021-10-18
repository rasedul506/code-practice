class Solution:
    def countPrimes(self, n: int) -> int:        
        if n == 0 or n == 1: return 0
        p = 2
        
        isPrime = [True for _ in range(n)]
        
        while p*p <=n:
            if isPrime:
                for i in range(p*p,n,p):
                    isPrime[i] = False
            p+=1
        return isPrime.count(True)-2
