# Merge sort with O(n Log n)

def mergesort(lst: list):
  if not lst: return None
  length = len(lst)

  if length > 1:
    med=length//2
    LST=lst[:med]
    RST=lst[med:]

    mergesort(LST)
    mergesort(RST)

    i=j=k=0

    while i<len(LST) and j<len(RST):
      if LST[i]<RST[j]:
        lst[k]=LST[i]
        i+=1
      else:
        lst[k]=RST[j]
        j+=1
      k+=1
    while i<len(LST):
        lst[k]=LST[i]
        i+=1
        k+=1
    while j<len(RST):
        lst[k]=RST[j]
        j+=1
        k+=1
    return lst
# to avoid duplicate value
#     newset = set()
#     for i in lst:
#       newset.add(i)
#     return newset

        

newlist=[2,5,4,1,6,7,8,2,5,1]
print(mergesort(newlist))
