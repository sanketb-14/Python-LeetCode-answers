# implementation of Open Addressing in python


class MyHash:
  def __init__(self , c):
    self.cap = c
    self.table = [-1] * c
    self.size=0
  def hash(self , x):
    return x % self.cap
  def insert(self , x):
    if self.size == self.cap:
      return False
    if self.search(x) == True:
      return False
    i = self.hash(x)
    t.self.table

  def search(self , x):
    h = self.hash(x)
    t = self.table
    i= h
    while t[i] != -1:
      if t[i] == x:
        return True
      i = (i + 1) % self.cap
      if i == h:
        return False
    return False    
      

  def remove(self , x):
    

 
    
  