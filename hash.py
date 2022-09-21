# to get index where key-value pair is going to be stored
class Hash:
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values =[None] * self.size
        
    def hash_function (self,key):
        # for adding characters in the key j+u+n+e using the ascii values
        sum = 0 
        # for iterating through every single character in the key
        for i in range(len(key)):
            sum = sum + ord(key[i]) #ord(key[iee])->going to transform characters into intergers and sum them up
            return sum % self.size

    def put(self,key,data):
        #to generate the index we pass the key in the hash function
        index = self.hash_function(key)
        
        #while the index allocation is not None
        while self.keys[index] is not None:
            # find another empty slot
            if self.keys[index] == key:#that the same key has been inserted in the same data structure
                self.values[index] = data #then we overide the old value with the new one
                return
            index = (index + 1)%self.size#move to the next slot/index
        
        #if we have the next empty slot
        self.keys[index] = key
        self.values [index] = data
        
    def get(self,key):
        index = self.hash_function(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1)%self.size
        return None#if its None
    
Hash1 = Hash()
Hash1.put("mazda",2012)
Hash1.put("toyota",2020)
Hash1.put("demio",2022)
Hash1.put("demio",2009)

print(Hash1.get("mazda"))
print(Hash1.get("demio"))

    
        
        