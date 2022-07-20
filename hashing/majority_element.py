def majorityEle(arr):
  m={}
  for i in arr:
    m[i] = m.get(i , 0) + 1  
  for i in m:
    if m[i] > (len(arr) // 2):
      return i
  
  
    
    
  
 
      
      
    
    

print(majorityEle([3,2,3]))
  