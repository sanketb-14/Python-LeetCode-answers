#window function for max_sum
def moveZeroes(arr,n,k):
  window_sum=sum([arr[i] for i in range(k)])
  max_sum=window_sum
  for i in range(n-k):
    window_sum = window_sum - arr[i] + arr[i +k]
    max_sum = max(window_sum , max_sum)
  return max_sum
    
    
  


print(moveZeroes([80,-50,90,100],4,2)) 