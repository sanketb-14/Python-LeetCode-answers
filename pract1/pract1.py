class Solution:
    #Function to return non-repeated elements in the array.
    def printNonRepeated(self,arr,n):
        dict={}
        for i in arr:
            dict[i]=0
            
        #storing the frequency of each element.
        for i in arr:
            dict[i]+=1
        
        l = []
        #iterating over the array elements.
        for i in arr:
            #if frequency of current element is 1,
            #then we store it in the list.
            if dict[i]==1:
                l.append(i)
                
        #returning the list.   
        return l

   printNonRepeated(self,[1,1,2,3,4,5,5,6,7] , 9)