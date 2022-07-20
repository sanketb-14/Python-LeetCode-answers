def maxArea(height):
  maxw=0
  i=0
  l=len(height) -1
  while(i < l):
    maxw=max(maxw , min(height[i],height[l])* (l - i))
    if(height[i]< height[l]):
      i+=1
    else:
      l -= 1
  return maxw  
  
   
  
    
    
    
     
    
  
    



  
print(maxArea([3,9,3,4,7,2,12,6]))  