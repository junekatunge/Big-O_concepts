class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in s:
            s_map[i] = s_map.get(i, 0) + 1
        for i in t:
            t_map[i] = t_map.get(i,0) + 1
         #after adding the elements on the list compare if the elements are the same  
        if s_map == t_map:
            return True
        else:
            return False