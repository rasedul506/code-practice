class Solution:
    def isHappy(self, n: int) -> bool:
        if n==0: return False
        newset=set()
        while n!=1:
            n=sum(int(digit)**2 for digit in str(n))
            if n in newset:
                return False
            newset.add(n)
        return True
