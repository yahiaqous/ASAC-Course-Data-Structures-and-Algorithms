def quick_sort(list,left,right):
  if len(list):
    if left<right:
      position = partition(list,left,right)
      quick_sort(list,left,position-1)
      quick_sort(list,position+1,right)
  return(list)

def partition(list,left,right):
  pivot=list[right]
  low=left-1
  for i in range(left,right):
    if list[i]<=pivot:
      low+=1
      swap(list,i,low)
  swap(list,right,low+1)
  return (low+1)

def swap(list,i,low):
  temp=list[i]
  list[i]=list[low]
  list[low]=temp

if __name__=='__main__':
  list = [8,4,23,42,16,15]
  quick_sort(list,0,5)
  print(list)
