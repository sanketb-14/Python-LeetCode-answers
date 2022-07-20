def printNonRepeated(arr):
  dict = {}
  for i in arr:
    dict[i] = 0
  for i in arr:
    dict[i] += 1
  l=[]
  for i in arr:
    if dict[i]==1:
      l.append(i)
  if l==[]:
    return -1
  else:
    return l[0]
  
    
  


print(printNonRepeated('aasssbb'))