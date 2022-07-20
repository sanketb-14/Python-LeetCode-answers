def subArraySum(arr,s):
  m={}
  for i in range(len(arr)):
    goal = s - arr[i]
    if goal in m:
      return [m[goal],i]
    m[arr[i]] = i
    
      
  
    
     
 
  
  
      
  
  
  
    
    
    
  



print(subArraySum([3,6,12,14],15))