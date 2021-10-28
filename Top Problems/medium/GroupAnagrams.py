class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         s2=[]
#         dict={}
#         for s in strs:
#             s1=''.join(sorted(s))
#             dict[s1]=dict.get(s1,[])+[s]
#         for i in dict.values():
#             s2.append(i)
        
#         return s2
        s2=[]
        dic={}
        for s in strs:
            self.binding(s,dic)
        for i in dic.values():
            s2.append(i)
        return s2
            
        
    def binding(self,word,dic):
        bucket=[0]*26
        for letter in word:
            pos=ord(letter)-97
            bucket[pos]=bucket[pos]+1
        s=''.join(str(x) for x in bucket)
        
        dic[s]=dic.get(s,[])+[word]  
