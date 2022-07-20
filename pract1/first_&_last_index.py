def search(list , target):
  left=0
  right = len(list) - 1
  while(left <= right):
    mid=(left + right) // 2
    if(list[mid] == target):
      if(mid == 0 or list[mid - 1] != target):
        return mid
      right=mid-1
    elif(target > list[mid]):
      left=mid +1
    else:
      right= mid - 1
  while(left <= right):
    mid2=(left + right) // 2
    if(list[mid2] == target):
      if(mid2 == len(list)- 1 or list[mid2 + 1] != target):
        return mid2
      left=mid2 + 1 
    elif(target > list[mid2]):
      left=mid2 +1
    else:
      right= mid2 - 1
  a=[mid,mid2]    
  return a 
    
      


print(search([5,8,8,8,8,18] , 8)) 