from optparse import Values


class Hash:
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size
    
    def hash_function(self,key):
        sum = 0
        for i in range (len(key)):
            sum =  sum +ord(key[i])
            return sum % self.size
    
    def put(self,key,data):
        index = self.hash_function(key)
        
        if self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data
                
            index = (index + 1)%self.size 
        self.keys[index] = key
        self.values[index] = data
        
    def get(self,key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index =(index + 1)% self.size
            return self.values[index]
        return None
    
        
    
  
            
        
        
h1 = Hash()
h1.put("cows","beef")
h1.put("pig","pork")
h1.put("sheep","mutton")
print(h1.get("pig"))

            
        
            