class Solution:
    def countAndSay(self, n: int) -> str:
        s='1'    
        while n>1:
            newstring=''
            i=j=0
            count=0
            while j<len(s):
                if s[i]==s[j]:
                    count+=1
                    j+=1
                else:
                    newstring+=str(count)+s[i]
                    i=j
                    count=0
            newstring+=str(count)+s[i]
            s=newstring
            n-=1
        return s
