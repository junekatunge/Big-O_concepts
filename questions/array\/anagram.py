class Solution:
    #the length of the string should be the same and the occurence of the occurence of the character should be similar forr both strings
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        #make a count of elements in each strings for example how many times i's  
        for i in s:
            s_map[i] = s_map.get(i, 0) + 1 
        for i in t:
            t_map[i] = t_map.get(i, 0) + 1

        for i in s:
            s_map[i] = s_map.get(i, 0) + 1

         #after adding the elements on the list compare if the elements are the same  
        if s_map == t_map:
            return True
        else:
            return False