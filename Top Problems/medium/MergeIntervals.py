class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        res=[]
        intervals.sort()
        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            last=res[-1]
            if last[1]>=interval[0]:
                last[1]=max(last[1],interval[1])
            else:
                res.append(interval)
        return res
                     
