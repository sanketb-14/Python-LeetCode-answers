 def findHashed(self,s):
        return "".join(sorted(s))
    def groupAnagrams(self, strs):
        ans= []
        m={}
        for s in strs:
            hashed = self.findHashed(s)
            if hashed not in m:
                m[hashed]=[]
            m[hashed].append(s)
        for b in m.values():
            ans.append(b)
        return ans 
  
  

       
    
    
  
  
   
print( groupAnagrams(["eat","tea","tan","ate","nat","bat"]))