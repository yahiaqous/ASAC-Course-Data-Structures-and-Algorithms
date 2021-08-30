def merge_sort(list):
  n = len(list)
  if n !=0:
    if n>1:
      mid = round(n/2)
      left=[]
      right=[]
      for i in range(mid):left.append(list[i])
      for i in range(n-mid):right.append(list[mid+i])
      merge_sort(left)
      merge_sort(right)
      merge(left, right, list)
  return(list)

def merge(left, right, list):
  i=0
  j=0
  k=0
  while i<len(left) and j<len(right):
    if left[i]<=right[j]:
      list[k]=left[i]
      i+=1
    else:
      list[k]=right[j]
      j+=1
    k+=1

  if i==len(left):
    while k != len(left)+len(right):
      list[k]=right[j]
      k+=1
      j+=1
  else:
    while k != len(left)+len(right):
      list[k]=left[i]
      k+=1
      i+=1

if __name__=='__main__':
  print(merge_sort([8,4,23,42,16,15]))
