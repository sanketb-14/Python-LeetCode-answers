def valid(arr):
  l=len(arr)
  left=-1
  top=max(arr)
  tindex=arr.index(top)
  right=top
  
 
  
      
  if (tindex ==0 or tindex== l-1):
    return False
  for i in range(0,tindex):
    if (arr[i] <= left):
      return False
      break
    left =arr[i]
  for i in range(tindex+1,l):
    if arr[i] >= right:
      return False
      break
    right=arr[i]
  return True

print(valid([0,2,3,3,5,2,1,0]))         